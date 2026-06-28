const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1280, height: 1000 }, deviceScaleFactor: 2 });
  const errors = [];
  page.on('console', m => { if (m.type()==='error') errors.push(m.text()); });
  page.on('pageerror', e => errors.push('PAGEERROR: '+e.message));
  const url = 'file://' + process.cwd() + '/report/research-report/index.html';
  await page.goto(url, { waitUntil: 'networkidle' });
  await page.waitForTimeout(800);
  // Verify the register actually rendered cards from improvements.js
  const expCount = await page.$$eval('#reg-experience .imp-card', els => els.length).catch(()=>0);
  const techCount = await page.$$eval('#reg-technical .imp-card', els => els.length).catch(()=>0);
  const impLoaded = await page.evaluate(() => (window.IMPROVEMENTS||[]).length);
  console.log('window.IMPROVEMENTS length:', impLoaded);
  console.log('experience cards rendered:', expCount);
  console.log('technical cards rendered:', techCount);
  // full-page screenshot
  await page.screenshot({ path: 'scratchpad/report_full.png', fullPage: true });
  // open a modal and screenshot
  await page.click('#reg-experience .imp-card');
  await page.waitForTimeout(400);
  const modalVisible = await page.evaluate(()=>!document.getElementById('modal').hidden);
  console.log('modal opens on card click:', modalVisible);
  await page.screenshot({ path: 'scratchpad/report_modal.png' });
  console.log('CONSOLE ERRORS:', errors.length ? JSON.stringify(errors,null,2) : 'none');
  await browser.close();
})();
