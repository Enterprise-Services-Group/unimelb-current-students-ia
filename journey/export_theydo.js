const fs = require('fs');
const crypto = require('crypto');

// 1. Read HTML and extract JOURNEY object
const htmlPath = './course-planning-enrolment-journey-map.html';
const htmlContent = fs.readFileSync(htmlPath, 'utf8');

// Use a regex to extract the JOURNEY object
const match = htmlContent.match(/const JOURNEY = (\{[\s\S]*?\n\});\n\n\/\* ---------- renderer/);
if (!match) {
  console.error("Could not find JOURNEY object in HTML");
  process.exit(1);
}

// Evaluate the object to use it
const JOURNEY = new Function(`return ${match[1]}`)();

// 2. Data stores
const data = {
  journeys: [],
  personas: [],
  steps: [],
  insights: [],
  opportunities: [],
  solutions: []
};

// 3. Helpers
const genLink = (item) => `${item.id}:${item.title}`;

// 4. Build Persona
const persona = {
  id: crypto.randomUUID(),
  title: JOURNEY.persona.name,
  bio: JOURNEY.persona.detail
};
data.personas.push(persona);

// 5. Build Journey
const journey = {
  id: crypto.randomUUID(),
  title: "Course Planning & Enrolment Journey",
  description: "Journey map focused purely on the course planning and enrolment experience for current students.",
  type: "L2",
  status: "active",
  personas: [persona]
};
data.journeys.push(journey);

// We need a lookup for insights/opportunities to avoid duplicates and map them correctly
// The HTML maps specific texts to details, we'll create the entities based on the texts found in stages
const insightMap = new Map();
const oppMap = new Map();
const solMap = new Map();

// 6. Build Steps and linked entities
JOURNEY.stages.forEach((stage, index) => {
  const stepId = crypto.randomUUID();
  const step = {
    id: stepId,
    title: stage.name, // "Name" in CSV
    description: `Doing: ${stage.doing.join('; ')} | Feeling: ${stage.feeling}`,
    position: index,
    channels: [...stage.touchpoints, ...stage.systems].join('; '),
    experienceScores: `${stage.emotion} (Persona: ${persona.title})`,
    personas: [persona],
    linkedInsights: [],
    linkedOpportunities: [],
    linkedSolutions: []
  };

  // Process Insights (Pains)
  if (stage.pains) {
    stage.pains.forEach(painText => {
      let insight = insightMap.get(painText);
      if (!insight) {
        const details = JOURNEY.details[painText] || {};
        insight = {
          id: crypto.randomUUID(),
          title: painText,
          description: details.body || "",
          type: "pain",
          linkedSteps: []
        };
        insightMap.set(painText, insight);
        data.insights.push(insight);
      }
      insight.linkedSteps.push(step);
      step.linkedInsights.push(insight);
    });
  }

  // Process Opportunities (HMW)
  if (stage.hmw) {
    stage.hmw.forEach(hmwText => {
      let opp = oppMap.get(hmwText);
      if (!opp) {
        const details = JOURNEY.details[hmwText] || {};
        opp = {
          id: crypto.randomUUID(),
          title: hmwText,
          description: details.body || "",
          status: "open",
          linkedSteps: []
        };
        oppMap.set(hmwText, opp);
        data.opportunities.push(opp);
      }
      opp.linkedSteps.push(step);
      step.linkedOpportunities.push(opp);
    });
  }

  // Process Solutions
  if (stage.solutions) {
    stage.solutions.forEach(solText => {
      let sol = solMap.get(solText);
      if (!sol) {
        sol = {
          id: crypto.randomUUID(),
          title: solText,
          status: "proposed",
          linkedSteps: []
        };
        solMap.set(solText, sol);
        data.solutions.push(sol);
      }
      sol.linkedSteps.push(step);
      step.linkedSolutions.push(sol);
    });
  }

  data.steps.push(step);
});

// 7. Output Unified JSON
const outputDir = '../theydo_export';
if (!fs.existsSync(outputDir)) {
  fs.mkdirSync(outputDir);
}

// Convert circular references to simple link representations for JSON
const jsonOutput = {
  journeys: data.journeys.map(j => ({ ...j, personas: j.personas.map(p => p.id) })),
  personas: data.personas,
  steps: data.steps.map(s => ({
    ...s,
    personas: s.personas.map(p => p.id),
    linkedInsights: s.linkedInsights.map(i => i.id),
    linkedOpportunities: s.linkedOpportunities.map(o => o.id),
    linkedSolutions: s.linkedSolutions.map(so => so.id)
  })),
  insights: data.insights.map(i => ({ ...i, linkedSteps: i.linkedSteps.map(s => s.id) })),
  opportunities: data.opportunities.map(o => ({ ...o, linkedSteps: o.linkedSteps.map(s => s.id) })),
  solutions: data.solutions.map(s => ({ ...s, linkedSteps: s.linkedSteps.map(st => st.id) }))
};

fs.writeFileSync(`${outputDir}/theydo_data.json`, JSON.stringify(jsonOutput, null, 2));

// 8. Output CSVs
function escapeCSV(str) {
  if (str === null || str === undefined) return '';
  const s = String(str);
  if (s.includes(',') || s.includes('"') || s.includes('\n')) {
    return `"${s.replace(/"/g, '""')}"`;
  }
  return s;
}

function writeCSV(filename, rows) {
  if (rows.length === 0) return;
  const headers = Object.keys(rows[0]);
  let csv = headers.map(escapeCSV).join(',') + '\n';
  rows.forEach(row => {
    csv += headers.map(h => escapeCSV(row[h])).join(',') + '\n';
  });
  fs.writeFileSync(`${outputDir}/${filename}`, csv);
}

// Map back to flat CSV formats
const csvPersonas = data.personas.map(p => ({
  ID: p.id,
  Title: p.title,
  Bio: p.bio
}));

const csvJourneys = data.journeys.map(j => ({
  ID: j.id,
  Title: j.title,
  Description: j.description,
  Type: j.type,
  Status: j.status,
  Personas: j.personas.map(genLink).join('; ')
}));

const csvSteps = data.steps.map(s => ({
  ID: s.id,
  Name: s.title,
  Description: s.description,
  Position: s.position,
  Channels: s.channels,
  Experience_Scores: s.experienceScores,
  Insights: s.linkedInsights.map(genLink).join('; '),
  Opportunities: s.linkedOpportunities.map(genLink).join('; '),
  Solutions: s.linkedSolutions.map(genLink).join('; ')
}));

const csvInsights = data.insights.map(i => ({
  ID: i.id,
  Title: i.title,
  Description: i.description,
  Type: i.type,
  Steps: i.linkedSteps.map(genLink).join('; ')
}));

const csvOpportunities = data.opportunities.map(o => ({
  ID: o.id,
  Title: o.title,
  Description: o.description,
  Status: o.status,
  Steps: o.linkedSteps.map(genLink).join('; ')
}));

const csvSolutions = data.solutions.map(s => ({
  ID: s.id,
  Title: s.title,
  Status: s.status,
  Steps: s.linkedSteps.map(genLink).join('; ')
}));

writeCSV('personas.csv', csvPersonas);
writeCSV('journeys.csv', csvJourneys);
writeCSV('steps.csv', csvSteps);
writeCSV('insights.csv', csvInsights);
writeCSV('opportunities.csv', csvOpportunities);
writeCSV('solutions.csv', csvSolutions);

console.log("Export complete! Files written to ../theydo_export");
