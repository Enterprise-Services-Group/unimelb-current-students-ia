<!-- converted from Web Governance & Code blocks.docx -->

Web Governance & Code blocks-20260615_133555-Meeting Transcript
15 June 2026, 03:35am
27m 42s
Nick Miller started transcription
David Mulholland   0:03
that from the planning discussion as a way of just saying, like, let's get together, let's have a first go at trying to establish what we all mean, because I think that's probably the bit that we still haven't quite aligned on yet. So it was helpful that you sent through that.
Rey Takeshima   0:03
Structural.
But.
Nick Miller   0:19
Yeah.
David Mulholland   0:22
that email. So I actually want to use that as the guide for the conversation because I want and and maybe you can help me with some clarification. So.
Nick Miller   0:33
One.
David Mulholland   0:34
We'll start with that point, so...
And I'll just probably grab that one bit. So a custom code block approach isn't scalable or sustainable for student comms, given our ongoing capability and capacity and our need to preserve our relationships and support model with DXM.
Nick Miller   0:58
Yeah, do you want me to take that thing slightly or?
David Mulholland   0:59
So why?
Yeah, please, please do, please do, and then I've got questions.
Nick Miller   1:03
Yeah.
Okay, so I guess the students, the current student site was moved into the matrix controlled environment templates in, I think, 2019, and...
Since then, we've gone through various peaks and troughs of custom code on the site. And...
We've kind of used it in the past for similar reasons to what we're talking about using it now, right? We head up against blocks in terms of what we want to do. Generally, the design system as it stands is kind of, in my view anyway, it suits itself, it lends itself to kind of sort of brochure style promotional sites and not so much to kind of service or task bounds.
types of content. So we're always hitting up against these kind of blockers in terms of wanting things to work in a certain way. And I guess the one consistent across that time has been that it's been very difficult to get anything into production with DXM. So we have done sort of custom code blocks.
David Mulholland   2:03
Yeah.
Nick Miller   2:08
across the site in the past. I guess the challenge, yeah, there have been a few challenges. One is probably consistency. So we might encounter like a specific use case for a custom code block and we might create a piece of CSS or a piece of JavaScript that fulfills a certain function.
But often it's just deployed to one location on the website, and it's not really done thinking about sort of wider use cases or wider application. So we might end up with layouts that look a certain way in one section of the website, and then that's not applied to the rest of the website, for example. So it has introduced inconsistency.
The second thing is just that because the design system is kind of current, is constantly a work in progress, the underlying structures and classes which it's built on are subject to change without any notice. So we'll get, we might modify an existing component and then a year later get an alert on the.
Squiz Slack channel that that component has been redeveloped with no warning, and it breaks everything that we had developed. And then we have to choose either to fix it urgently or to ditch our modification. And then I guess the third thing is that we're not really a technical team, right? We have web producers who know the design system and are responsible for building out pages using it.
But we don't.
We don't hire people based on their knowledge of coding at the moment and totally get that that's sort of becoming less relevant as we can get the machines to do it for us. But to a certain extent, you still kind of need someone who understands what to ask for and understands what quality looks like, I suppose, and what's sort of manageable.
David Mulholland   3:52
Da.
Nick Miller   3:56
And so generally, in those situations where we introduce custom code, design system changes, everything breaks, we're basically kind of cutting ourselves off from any support on that because as soon as someone from DXM looks at it, they'll say, well, you've got custom CSS here, we can't help you with that.
David Mulholland   4:09
Yeah.
Nick Miller   4:16
So it kind of immediately breaks the support model in a way that they, if you're experiencing troubles with a page and it's got custom code on it, they immediately will just say, no, we're not helping, regardless of whether or not the issues are related to the custom code. And also it kind of just degrades the relationship, right?
Because every time they sort of frown upon it and every time they see it, it means that you're in the bad books. So that's kind of the overall summary. And it's why, yeah, I sort of have a bit of a strong reaction. I 100% see the need for it. I just struggle to see how it becomes.
David Mulholland   4:56
Okay.
Nick Miller   4:58
Future-proof, I suppose.
David Mulholland   5:00
Yeah, so I think that there's a few things to...
that I'm keen to unpack. So the first one that maybe was that might be implicit but not explicit in your email.
Is.
you're kind of talking about maybe kind of the long-term approach. So I'm wondering whether that apply what you're saying also applies to short-term top time boxed tests.
Nick Miller   5:37
Yeah, so I feel differently about that because I think what my worry is that we become reliant on something that we can't sustain. Whereas kind of what Han is proposing with the help and support module at the moment is like, let's code something up, let's run an AB test, let's collect the results.
then let's present those back to DXM as part of the business case for doing this, right? And that I feel pretty positive about. So I'm happy to do those sort of short-term experiments with the proviso that like we have to have a fallback, basically. Like we can't be dependent on that for our digital.
Strategy, but as part of an experiment to kind of prove out a theory and use that as a business case to get something done, I think that makes perfect sense.
David Mulholland   6:23
I.
Yeah, because I yeah, I think that's that's important. So that's probably my first
thing that I'm, I think maybe we kind of look past each other on is just that point. I think what we want is the same thing. We want to be able to prove something out and then for it to be have our proof of concept, maybe collect data about the customer experience, analytics,
maybe have it be in there in enough time that we actually see some impact on inquiry volume, perhaps. And then for us to then have a kind of a checkpoint, like, do we want to do this? Do we now have enough evidence to progress it to become
Nick Miller   7:03
Yeah.
David Mulholland   7:15
like a proper module or is this something that's failed and we're like happy to put it, you know, go back to a fallback position of whatever the matrix EMS offers.
Nick Miller   7:25
Yeah, I think that makes total sense. And I think what would be super helpful as part of that is if we can develop the fallback option and the ideal option at the same time and test those against each other, then we have a really clear benchmark of, okay, if we take away the ideal option,
David Mulholland   7:26
Yeah.
Nick Miller   7:43
what results is the fallback option going to get us. We know the fallback option is doable within the design system. We know that we'll get better results with the ideal option, theoretically. Then we're making a kind of educated choice. So I like, that's why I kind of like this AB test option, because it gives us data on both.
I think if we just develop something custom and don't have a fallback option, and then we get to the end of our experiment period and the data's been really good, but we don't necessarily have an alternative, that I feel like could leave us in a bit of a tricky situation of, okay, design work's been done, we've borne out the design work, we know that it works.
But we're getting closer to our kind of closer to the end of the year and we don't have another option. And that puts us in a, I guess, between a rock and a hard place, particularly with project sponsors who are going to clearly, it's going to be very hard to explain to them why we're undoing design works that we know works and when we have no kind of fallback option to implement.
David Mulholland   8:41
Yeah.
Yeah, nice. All right, so we were definitely aligned on that, and I think that that's something that's completely doable.
Nick Miller   8:54
Yeah.
David Mulholland   8:56
The other things that I am keen to get your view on, what you mean by scalable and sustainable and what you mean by team capability and capacity is
And maybe if you could bring it to light, like you did mention.
that you've got kind of gone through these peaks and troughs, but is there a particular example of a recent code block that hasn't met like the team capability or capacity that I can that can kind of give me a bit more understanding?
Nick Miller   9:36
Yeah, I mean the obvious one is the course planning tree hash tool, I think, which like, I kind of probably over ambitiously was like, oh yeah, simple functionality, we've got something similar on the website at the moment, couple of drop downs and it, you know, defaults to an option based on what you've selected.
David Mulholland   9:37
Yeah.
Nick Miller   9:54
Really easy to code that up in Claude. Let's just implement that.
Then, the reality of having sort of...
Sixty-eight different outcomes, each with a different piece of content, all of which needed to be maintained within HTML, rather than, you know, using the easy-to-use interface of, for example, it just meant that when Matt and Stuart were building it out, it became really fiddly, and I guess that's particularly the case because...
Wild Matt and Stuart, no, you know.
pretty sort of simple to intermediate HTML and CSS, that if, you know, if something changes in that, like, oh, actually, we're going from 8 options in this list to five, and that changes the logic of how it all works, there becomes a kind of a back and forth with Claude to be like, okay, now I'm going to.
make this change, can you update the code for me, but now I have to update the content in the CMS and it kind of becomes like challenging for them. So I think Matt found that quite fiddly and he sort of explicitly sought me out towards the end of that build and was like, let's not do this again. So I think that that's the kind of.
David Mulholland   11:11
Yeah.
Yeah.
Nick Miller   11:14
Capability piece of it.
The capacity is probably more just around the fact that, like, if we have, I would say, like...
one or two of these pieces of code that we're reliant on on the site moving forward and we know what they are and we know where they're deployed and we have pretty clear rules around like, you know, how they were created and how they need to be maintained. That feels okay to me because it's, you know, if they break.
There's only one thing that we need to look at, and we might have to dedicate a bit of time to fixing it, but we can probably do that. My worry is, if we end up with, you know, 5, 6, 7 little pieces of code applied to different areas of the site, it becomes harder to kind of get a sense of...
if or when the design system is changing, what that impacts, what needs to be redeveloped, what needs to be tested. So I guess that's why when you were talking about the tags, Rey, I was kind of thinking, all right, well, if we have to do this, if we feel that it is really beneficial, how does it work across the whole site? Because I don't just want to apply it to one.
Area, I want anything that we develop to be kind of theoretically usable across the broader structure of the site.
Rey Takeshima   12:32
Yeah, absolutely. It sounds like there's some principles we could potentially follow here of just like decoupling dependency using the lessons learned from the triage tool of like exactly what Matt was talking about of updating content in one interface, updating code another, like just let's not let's not do that and make the experiments really bite-sized.
David Mulholland   12:46
Mm.
Nick Miller   12:50
And.
Yeah, yeah, and then, and then I think it's like, I'm happy to have, you know, several bite-sized experiments running. That's totally fine. I think it's, as you said before, David, it's that future-proofness for me. Like, if we decide there's something we're really reliant on and we want to bite the bullet and live with it.
David Mulholland   12:53
Yeah.
Nick Miller   13:10
ongoing and we can't get it productionized, then let's sort of keep those to the essential must-haves and keep the number pretty small.
David Mulholland   13:20
Yeah, so there's a few things that are in that if I can unpack maybe some potential solutions to that. So
So on the team capability thing, that to me reads that.
We just need to have some rules around the scope of what a code block is. Because like, yes, the code block, it will accept JavaScript and HTML and CSS and it will probably accept like 100 kilobytes of code. But we should agree, like similar to how you have.
kind of content authoring guidelines, we should just agree like what a code block should be and it shouldn't be in order to be.
Nick Miller   14:08
Mhm.
David Mulholland   14:13
fit within like the capability of the team. So like, for example, like an accordion.
Nick Miller   14:16
Mmh.
David Mulholland   14:20
Has, you know, a code snippet of four accordions. It's all HTML. OK, like tick that that kind of meets that good part of the criteria as soon as it's like logic that has more than three.
kind of if-then statements, it's like, no, this is not something that we're looking to support.
Nick Miller   14:44
Yeah.
Yeah, and I guess another thing to think about as part of that scoping would be like, does it leverage an existing class and modify an existing class, or are we defining a class to add on? Because in terms of that design system thinking, right, if you're leveraging an existing class and then overriding certain qualities or parts of it.
and that class then changes, you leave yourself susceptible to something breaking. However, I guess the advantage of doing that is that you're taking something that exists within the design system and making a minor modification rather than creating something new completely from scratch. The advantage of creating something new completely from scratch is you're not so dependent on the design system, but then if the design system changes, you have to redesign the part.
David Mulholland   15:16
Yeah.
Nick Miller   15:30
I think it's just worth thinking through some of those types of like eventualities and what is going to be the most future proof and what that means, as you say, from like a governance maintenance perspective.
David Mulholland   15:40
Yeah. And can I make a suggestion on that that I think one thing that I think we mentioned this as part of the previous chat is I think what we need is to spend some time and like document some of this and
Maybe just mature.
the current state, like before we even start doing anything else, let's just mature the current state. And the example of that is you've got code blocks for like the new starter checklist. Let's just like if we're treating this, the new starter checklist or that.
accept your offer page as one of the code blocks. Let's just document what the maintenance of that looks like and any other long-term code blocks.
Nick Miller   16:24
Yeah.
Yeah.
David Mulholland   16:35
And then that can be the model for, okay, this is essentially the template of how we manage code blocks. Now, how do we feel about managing more of these? If, you know, and then I suppose based on that, we can kind of reverse engineer and talk with Matt.
and co about what the rules are, like the leveraging existing classes and all of that type of detail.
Nick Miller   16:57
Yep.
I think that sounds really good. Yeah, and if we can sort of...
you know, as you say, do a bit of an audit of what we've got at the moment and sort of consult with Matt around like, okay, you've got to modify this tomorrow. How comfortable do you feel about that? And that will give us a sense of what we might need to start moving away from as well in terms of things that we already have that are maybe not super sustainable. Sorry, Rey.
David Mulholland   17:25
Yeah.
Taryn.
Rey Takeshima   17:29
No, not at all. I'm just patiently waiting because the point I wanted to make is kind of in addition to this thread there, Nick and David, I'm not talking about roles and responsibilities or capability or maturity uplift. I like the thing that you and I mostly connect on, Nick, is the specificity, like, like what is the exact thing?
that you might get out of each one of these proof of concepts, and it might be nice just to touch on that one. Like, let's say the help and support block use case is really tangible, right? We can definitively prove that this layout, this set of styling, these new content options make sense, and it might be nice to think about like for every.
proof of concept that we might do, like what is the intended sort of goal or outcome there? Is it to push for like a new backlog item with DXM? Yes, maybe that's the case in some of them, but maybe not all. Maybe some of them might be a depreciation of a convention that already exists within your team. I'll take the example of like...
the context nav component now is really coming up in terms of use at adoption. In page tabs, the like jump nav is now coming down a little bit. So with every experiment we do, it's kind of nice to think about that strategy of what is that end goal. And some of the options I can see aside from those two, like appreciation.
and depreciation of components might even just be like, like conventions, like maybe another one is you might need a standard or another one might be like we can now use or unlock this particular element within Matrix that we weren't really using all that much before. Like I don't know what the answers might be, but it might be nice to just align on what those things are. Yeah.
Nick Miller   19:08
For sure, for sure. Yep, no, I think that sounds good.
David Mulholland   19:12
Um...
The last thing that I wanted to show is.
A lot of the work that we're doing at the moment is actually we're dealing with the staff hub side of things within the service experience and design team. Like we're doing it IA overhauls of intranet sites, which can be a little bit interesting, a little bit dry dealing with kind of stuff.
services, but the interesting thing in dealing with Staff Hub is, I don't know if you've ever worked with that group like Alice Olenich and that team.
Nick Miller   19:41
But...
Sort of indirectly, yeah.
David Mulholland   19:58
Yeah, they what they've done to manage their.
their intranet design system is a couple of things. So just share this page. This has in the intranet, they have their design system documented here.
And then they have all of the components documented. They don't actually manage any of their content components as.
Content.
like CMS-able components, they manage them all as content blocks. And then this is how they kind of maintain them for use. So they have a design system, they have a code block widget where you can copy code.
They have all of the variations.
Um...
Just as you would expect, like a design system rationale.
usage. So the reason why I wanted to show this is for a couple of parts. One is...
It's interesting to see same CMS, two different implementations managed so differently. Like it's obvious the reason why that that.
21:24
Mm.
David Mulholland   21:31
I shouldn't say it's obvious. It actually wasn't obvious to me. I talked to Alice and she said, the reason why we manage it this way is because we've got a small team, it's centrally managed, and it's easier for us to manage it all in code blocks than fiddle around with content blocks.
Whereas the matrix controlled environment is because it's all distributed, you have all of these brochureware websites, like you said, and...
you know, people need to be trained up to use it. They don't need to know HTML. The thing about that I kind of maybe thought was interesting as well is your team is probably the unique case where you're a central team plus with distributed authorship.
Nick Miller   22:04
Big.
David Mulholland   22:18
So, like I was wondering whether that might relate to there being a bit of a hybrid governance arrangement for you.
Nick Miller   22:32
Yeah, it's an interesting one, isn't it? So, are you saying that, like, every time they build out a new section, the staff are they are assembling that?
David Mulholland   22:40
Yes.
Nick Miller   22:40
in a series of code blocks. Because I would say, yeah, the things that were running through my head when you were talking about that is like, yeah, it requires a high degree of control. And anecdotally, what I observe with Staff Hub is people are moving content off it because it's too hard to work with. So everyone's moving everything onto SharePoint because.
it's hard to get something created and hard to maintain it when it's on the staff hub. So for example, we used to have a staff hub section and it's all moved on to SharePoint now because it's easier to work with. So it's finding that balance, right? If you've got a small centralized team, do you actually have the capacity to manage all of that content for everyone and what do you need to outsource and how do you sustain that?
David Mulholland   23:12
Ha.
Yeah.
Nick Miller   23:21
And I guess in that sense, like using the existing design system with some modifications, I would say is a bit easier because people who have no technical literacy whatsoever can still use the CMS to create and publish content, but you're kind of applying those some specific rules selectively at a higher level, I guess, and keeping the code.
out of the content, like storing it elsewhere and choosing how it's deployed, which is kind of how we've generally done it in the past. But yeah, again, maybe it comes back to not having that governance. Different people do it differently. You lose track of where your code is. You don't necessarily have it all stored in like a central.
folder with a clear record of where it's deployed and displaying and so on.
David Mulholland   24:06
Yeah, that's also a very good point. The second point that I wanted to make on this is this would be a good example of how we could manage our code blocks and how we can say we were running an experiment and
As I was kind of talking about before, they kind of need to be long enough that we're testing multiple options, sometimes long enough where we're seeing if there's going to be impact on inquiry volume. So you'd want to kind of document the use of these and also kind of link to, hey, here's where
this has been added to. So it kind of talks to that point about maintainability. This is probably an example of something that we could create.
Nick Miller   24:46
Yeah.
Yeah, yeah, I think that sounds good. Conscious of time, but then, so in terms of next steps, I'd like to maybe just share a summary of this conversation with Matt and just talk it through with him as well, because in practice he's the person who will be doing a lot of this. And then, yeah, I know you'd spoken.
with Rahul around sort of doing a governance piece, maybe it's just worth us having a conversation around what that looks like in terms of maybe sort of figuring out what we've got now, documenting some of the stuff that we've talked about today, maybe consulting with Matt and Stuart and James and kind of understanding their capability and capacity.
David Mulholland   25:32
I.
Nick Miller   25:32
Responding to that.
David Mulholland   25:33
Yeah, I think that's a good next step. Maybe the interview with Matt and the team might be a good.
Rahul Grover   25:34
Yeah, so.
Yeah.
David Mulholland   25:42
first step and then the governance.
maybe towards sometimes next week or...
Nick Miller   25:49
Yeah.
David Mulholland   25:50
You can have another follow-up.
Nick Miller   25:51
Why don't I, I'll book in a time to chat with Matt and Stuart and James and give them a heads up and then Rahul if you wanted to, oh sorry, do you want to jump in?
Rahul Grover   25:52
Just.
I was just going to say that I already started a draft document to sort of put my thoughts on paper and I've shared with you all. And yeah, it's just a draft at the moment just to sort of have some points around what I'm thinking, what the framework would look like, but I think it needs to be updated after these conversations are being held and what comes out of it. And then
Yeah, we take something out that doesn't apply to us, and we'll add something that we think is a better idea. For example, the A/B testing, I had it pitched differently, but there was a fallback mechanism, but it's good to sort of test it if there isn't any. What does the current design system or more feasible design system that we know that we can achieve with the components will look like?
B form of the same thing, and that becomes if in three months' time, for example, we find it's not working or whatever, that's a clear pathway to take then, and it's all already in place, so yeah, I can update that.
Nick Miller   26:54
Yeah, that sounds good. And I guess it's like, I just want to be in a position whereby if we don't have a fallback and we deploy something on the website and we see a significant drop in inquiries, then I need to be able to have an honest conversation with Kate to be like, look, we've done something here and we've got no alternative option to fall back on, but it's not sustainable. You know, maybe she can lobby for that at DXM at a higher level, or maybe, you know, it's just talking about what that looks like.
David Mulholland   27:16
That's what I'm.
Yeah, yeah, let's keep talking about that and the DXM. We didn't cover DXM in this chat. We'll bring that into another chat.
Nick Miller   27:20
Yeah.
Rahul Grover   27:21
Yeah.
Nick Miller   27:28
Yeah, cool. David, have you got to run?
Rahul Grover   27:30
Sorry about me dropping out and about.
David Mulholland   27:32
Yeah, no, I'll stay. I'll stay on.
Nick Miller   27:35
Okay, cool. Thanks. All right. Thanks, Rey. Thanks, Rahul.
Rahul Grover   27:37
I'll drop off, but sorry about dropping off early as well. Not intentional. See ya.
Nick Miller   27:40
Okay, see you soon.
Rey Takeshima   27:41
All good. See you later. Bye.
David Mulholland stopped transcription