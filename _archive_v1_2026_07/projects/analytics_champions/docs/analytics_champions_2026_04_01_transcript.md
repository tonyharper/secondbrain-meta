# Analytics Champions [Rescheduled] - April 1, 2026, 9:35-10 AM PDT [AI meeting transcript by Zoom]

*AI Generated Document. Please note that this working copy of the transcribed meeting is AI-generated and is thus subject to error.  As this working document is subject to edits, it may not always accurately reflect the contents of the meeting.*





Invitees: Tony Harper, Shawn Peters, Syed Hasan, Steve Fischer, Engin Sözer, Vibha Virmani, Narendra Kambam, Parth Parekh, Ryan Sullivan, Kody Bartelt, Omri Ziv, Alex Ryckman Mellnik, Roy Avraham, Erik Gregory, Matt Hartwig, Ed Riviere, Travis White, Elaine Wang, Tracie Cheung, Tony Cantin, Qiang Yang, Thasneem Farzana, Karthik Lakshminarayanan, Angeli Kirk, Nicole Buttermore, Megan Farwell


00:00:22.000 --> 00:00:24.000 Narendra Kambam: Steve.


00:00:23.000 --> 00:00:25.000 SEA - Caffe Vita: Hey Norenda, how are you?


00:00:25.000 --> 00:00:27.000 Narendra Kambam: Fantastic, yourself?


00:00:27.000 --> 00:00:30.000 SEA - Caffe Vita: All right. All right.


00:00:28.000 --> 00:00:34.000 Narendra Kambam: That long sign means a lot, Steve.


00:00:31.000 --> 00:00:37.000 SEA - Caffe Vita: Uh, yeah, oh boy. Yeah, interesting times.


00:00:38.000 --> 00:00:43.000 Narendra Kambam: Yeah, that's the… that's the one, like, couple of words I keep hearing.


00:00:43.000 --> 00:00:45.000 Narendra Kambam: To anyone I talk to.


00:00:45.000 --> 00:00:50.000 SEA - Caffe Vita: Yeah, it's, uh… I don't know. I honestly, I think, like, this will…


00:00:50.000 --> 00:00:52.000 Narendra Kambam: Mm.


00:00:50.000 --> 00:00:54.000 SEA - Caffe Vita: You know, we'll remember these days, like, it's just so…


00:00:53.000 --> 00:00:55.000 Narendra Kambam: Yeah.


00:00:55.000 --> 00:01:00.000 SEA - Caffe Vita: You know, 25 years software and data engineering, you know, never anything like this.


00:00:59.000 --> 00:01:02.000 Narendra Kambam: Yeah, exactly, yep, yep.


00:01:01.000 --> 00:01:02.000 SEA - Caffe Vita: So…


00:01:18.000 --> 00:01:20.000 BEL - 1 way vs. 2 way door: It helps.


00:01:50.000 --> 00:01:52.000 BEL - 1 way vs. 2 way door: Get people a little more to join.


00:01:56.000 --> 00:01:59.000 SEA - Caffe Vita: Tony, so you're gonna be at Dexter tomorrow and Friday, is that right?


00:01:58.000 --> 00:02:00.000 BEL - 1 way vs. 2 way door: Yeah, yeah.


00:01:59.000 --> 00:02:01.000 SEA - Caffe Vita: Cool. Alright.


00:02:07.000 --> 00:02:08.000 traciecheung: Hey guys, happy Wednesday.


00:02:08.000 --> 00:02:10.000 BEL - 1 way vs. 2 way door: Same.


00:02:11.000 --> 00:02:13.000 BEL - 1 way vs. 2 way door: Can I give…


00:02:13.000 --> 00:02:16.000 BEL - 1 way vs. 2 way door: A few more minutes for people to join. We'll get started.


00:02:31.000 --> 00:02:33.000 BEL - 1 way vs. 2 way door: And then…


00:02:35.000 --> 00:02:39.000 BEL - 1 way vs. 2 way door: Ryan and Alex can't make it, or Alex will be late.


00:02:42.000 --> 00:02:44.000 BEL - 1 way vs. 2 way door: Let's see if there's any other…


00:02:44.000 --> 00:02:51.000 BEL - 1 way vs. 2 way door: commenters in the doc, really. Okay, let's go ahead and get started. Um, I wanted to go through the…


00:02:51.000 --> 00:02:58.000 BEL - 1 way vs. 2 way door: champions and SME group model. This is more for the DEs, although DEI folks, you're welcome to weigh in, but um…


00:02:58.000 --> 00:03:03.000 BEL - 1 way vs. 2 way door: And then we'll do the second topic, which is the, uh, DataX survey results, which are very exciting.


00:03:03.000 --> 00:03:08.000 BEL - 1 way vs. 2 way door: Um, okay, so on the analytics Champions and Speed Group model, I think we can break this into two pieces.


00:03:08.000 --> 00:03:19.000 BEL - 1 way vs. 2 way door: the first thing I think we should talk about is which SME groups, like, what do we want to do with the SME groups? Like, I think… I don't think anybody was saying, no, no, no, they're perfect as it is. So I think that we're aligned that there's work to be done there.


00:03:19.000 --> 00:03:26.000 BEL - 1 way vs. 2 way door: Um, I want to see if we can align on which ones are worth keeping… which ones need to be fixed, which ones we should get rid of.


00:03:26.000 --> 00:03:32.000 BEL - 1 way vs. 2 way door: Um, here. And then the second… then if we can talk a little bit about what we want to do as a champions group, that'd be useful.


00:03:33.000 --> 00:03:49.000 BEL - 1 way vs. 2 way door: So let me kind of go through what I've seen, uh, from the comments. I think we all agree data visualization is… or slash consumption is still needed. I don't think there's any controversy there. Nest is exploding, that's amazing, we all love it, but, like, you know, it's like going in new directions, and we need to steer and shape that.


00:03:49.000 --> 00:03:57.000 BEL - 1 way vs. 2 way door: Um, my thinking here is we keep… we probably need to, like, figure out what we're doing there, which we have the right people, but we generally keep that group. Any disagreement? Vibha, go ahead.


00:03:57.000 --> 00:04:04.000 Vibha Virmani: No disagreement, but I just wanted to let you know that Dinkar, under Dinkar, Ravi, and I think…


00:04:04.000 --> 00:04:16.000 Vibha Virmani: I forgot the PM name. They're already working on Nest, and there is some collaboration going on. My team specifically is working on some collaboration with them, so I think the sooner we create a group where there is a.


00:04:16.000 --> 00:04:25.000 Vibha Virmani: Participation from all the pillars will be good, because as of now, like, 3 or 4 members of my team are working on it, uh, with them.


00:04:18.000 --> 00:04:20.000 BEL - 1 way vs. 2 way door: Yep.


00:04:24.000 --> 00:04:28.000 BEL - 1 way vs. 2 way door: Yep. I'm meeting Dinka earlier today, I'll talk about him on this topic.


00:04:28.000 --> 00:04:31.000 BEL - 1 way vs. 2 way door: So, okay, good on that one.


00:04:31.000 --> 00:04:36.000 BEL - 1 way vs. 2 way door: Um, semantic models and evals, there is something going on there.


00:04:36.000 --> 00:04:41.000 BEL - 1 way vs. 2 way door: There might actually, in fact, be an organically built SME group on that already.


00:04:41.000 --> 00:04:48.000 BEL - 1 way vs. 2 way door: with participation from, like, all of the things, all of the pillars. Um, I know Chris Ventura from my team's involved.


00:04:48.000 --> 00:04:58.000 BEL - 1 way vs. 2 way door: I know we've got folks from Instagram, from, um, RL and others involved. I wonder… I'm kind of hesitant to go, like, create a new thing there, because, like.


00:04:58.000 --> 00:05:05.000 BEL - 1 way vs. 2 way door: there's a DE and DI group moving all that ahead. I think I just want to draw a line around that and call that the SME group and move on.


00:05:06.000 --> 00:05:16.000 BEL - 1 way vs. 2 way door: Um, I'll get some… I'll get some answers about who's involved there, and we can see if we feel like we've got any major gaps, like, if someone is not connected, we can fix that, but I think it seems like a pretty strong group.


00:05:18.000 --> 00:05:24.000 Narendra Kambam: And that's the same group, right? The semantic model work stream you're referring to, Tony? Uh, with, uh…


00:05:23.000 --> 00:05:29.000 BEL - 1 way vs. 2 way door: So, it's Matt Hartwig is the PM, Shreyer, and then a collection of DI and DE folks there.


00:05:25.000 --> 00:05:27.000 Narendra Kambam: Yeah.


00:05:29.000 --> 00:05:31.000 Narendra Kambam: Correct, okay, yep, that's the one, okay.


00:05:30.000 --> 00:05:38.000 BEL - 1 way vs. 2 way door: I don't feel any… I think I'm like, just… please keep going, guys, like, I don't feel any need to do surgery on that, although we should probably just put some, like, you know.


00:05:38.000 --> 00:05:41.000 BEL - 1 way vs. 2 way door: Documented, basically.


00:05:40.000 --> 00:05:42.000 Narendra Kambam: Yeah.


00:05:40.000 --> 00:05:47.000 Vibha Virmani: Uh, actually, what will happen, Tony, once we will dig deeper into it.


00:05:47.000 --> 00:05:58.000 Vibha Virmani: this model… this group was created, like, somebody came up with the idea, then some people were passionate about it, they started working with them, so that's how the group is. It's not following those standard models of.


00:05:58.000 --> 00:06:10.000 Vibha Virmani: Uh, like, how we were creating the group. I'm not sure if we need to or not. I know that some people are from, like, FBIP and my team, and there are all over the place, and there are more than one person also in each pillar here.


00:06:03.000 --> 00:06:05.000 BEL - 1 way vs. 2 way door: Yep.


00:06:09.000 --> 00:06:11.000 BEL - 1 way vs. 2 way door: Right.


00:06:10.000 --> 00:06:12.000 Vibha Virmani: Um… yeah.


00:06:11.000 --> 00:06:16.000 BEL - 1 way vs. 2 way door: I think that's fun, but I think it's fine. I don't… I'm not… I don't feel like we need to impose the structure on it. If they're doing good work.


00:06:15.000 --> 00:06:17.000 Vibha Virmani: Got it.


00:06:16.000 --> 00:06:18.000 BEL - 1 way vs. 2 way door: Great.


00:06:18.000 --> 00:06:23.000 Vibha Virmani: Yeah, that's… that's just wanted to… wanted everybody to be aware of it in case, like.


00:06:23.000 --> 00:06:30.000 Vibha Virmani: It's generally good to have at least some documentation that who's leading the group, who are involved.


00:06:30.000 --> 00:06:32.000 BEL - 1 way vs. 2 way door: Yep.


00:06:30.000 --> 00:06:33.000 Vibha Virmani: But it's okay not to put the structure, that is totally fine with me.


00:06:33.000 --> 00:06:49.000 BEL - 1 way vs. 2 way door: the thing I want to put pressure test on that one is, is it, like, I think it's working pretty well for semantic models. Are they actually covering evals? I don't know. And if they're not, what do we need to do on that? There is some DI versus CPP stuff on the eval thing as well, that we can dig into, but look, we can start documenting that one and go from there.


00:06:51.000 --> 00:07:00.000 BEL - 1 way vs. 2 way door: Okay, um, data warehouse… warehouse… data processing warehouse internals. I don't know what's going on with that group now. I think we all agree it needs to continue to exist.


00:07:00.000 --> 00:07:03.000 BEL - 1 way vs. 2 way door: Um, is anybody close to that? Does anybody know?


00:07:04.000 --> 00:07:17.000 Vibha Virmani: I think the last part I am aware of is, was the capacity one, which, like, kind of still, uh, involves some things here and there, uh, with the new model, how we are doing a DWH capacity, uh, compute and storage.


00:07:17.000 --> 00:07:28.000 Vibha Virmani: But that's… that's the only part which I've heard is… is in work and keeps on changing. And I'm not sure that is this gonna be the same group who will eventually manage the…


00:07:28.000 --> 00:07:32.000 Vibha Virmani: Cloud tokens and all, but capacity management, we should keep it for now.


00:07:30.000 --> 00:07:32.000 BEL - 1 way vs. 2 way door: Yeah.


00:07:32.000 --> 00:07:35.000 BEL - 1 way vs. 2 way door: Yeah, okay, we can dig in and just see what's going on there.


00:07:35.000 --> 00:07:42.000 BEL - 1 way vs. 2 way door: tweaks needed. So, in the cloud stuff, it'll come to us one way, I'm sure, and we'll have to react to it. So, for now, it seems free.


00:07:43.000 --> 00:07:48.000 BEL - 1 way vs. 2 way door: So, we'll see. Okay, um, moving on to the next ones, privacy and security.


00:07:48.000 --> 00:07:53.000 BEL - 1 way vs. 2 way door: I did change my mind on that, thank you for the feedback, we can keep that, so… it's…


00:07:53.000 --> 00:08:02.000 BEL - 1 way vs. 2 way door: We had a feedback session the other day, it seems to have gone well, so we'll just keep doing that one. If you guys have feedback for me on that one, I'll take it. Otherwise, we'll just keep running.


00:08:02.000 --> 00:08:11.000 BEL - 1 way vs. 2 way door: Um, metric trust and governance, Engin, you're… you're closer to this than I am. I'm not really sure what's going on here, if anything.


00:08:12.000 --> 00:08:13.000 Engin Sozer: Yeah, honestly, like…


00:08:14.000 --> 00:08:33.000 Engin Sozer: from the beginning, I didn't like, actually, we are calling this metric trust and data governance. So, I'm not… I'm not really keen on keeping it that way, but I think there is… there's definitely a good element of data governance that we should keep, right? Like, currently, like, we are doing a lot now in semantic models, but there's a lot of, like.


00:08:33.000 --> 00:08:38.000 Engin Sozer: investment in the overall warehouse governance as well, and this is becoming more and more critical.


00:08:38.000 --> 00:08:45.000 Engin Sozer: Uh, I'm not sure if it's worth actually exploring the option of making this AI and data governance, because.


00:08:45.000 --> 00:08:50.000 Engin Sozer: We all know that we are suffering from AI governance itself, which might actually be an opportunity.


00:08:50.000 --> 00:09:00.000 Engin Sozer: Uh, but I'm, I'm definitely reposition, like, I'm definitely in favor of repositioning, uh, rebranding this group, but keeping it.


00:09:00.000 --> 00:09:04.000 BEL - 1 way vs. 2 way door: Okay, can you take a pass on that, Engin? Come back to us?


00:09:04.000 --> 00:09:05.000 Engin Sozer: Absolutely, yep.


00:09:05.000 --> 00:09:09.000 BEL - 1 way vs. 2 way door: Fantastic. Alright, experimentation…


00:09:11.000 --> 00:09:16.000 BEL - 1 way vs. 2 way door: I don't know, what do you all think? My group doesn't… we don't do much experimentation in risk, so I'm kind of disconnected here.


00:09:17.000 --> 00:09:22.000 Narendra Kambam: Yeah, same here. We do a little less than compared to other product pillars.


00:09:22.000 --> 00:09:29.000 Shawn Peters: And isn't this one… hasn't this one always been sort of driven on the side a little bit, like, directly with that team?


00:09:23.000 --> 00:09:24.000 Engin Sozer: Um, my.


00:09:27.000 --> 00:09:32.000 BEL - 1 way vs. 2 way door: Yeah. With Central Products. It's not a DI, they're not DI, yeah.


00:09:31.000 --> 00:09:39.000 Engin Sozer: Yeah, that's what I would say as well, like, I… we never could actually crack on that problem, and I don't think we will be able to.


00:09:31.000 --> 00:09:33.000 Shawn Peters: Right.


00:09:40.000 --> 00:09:47.000 Shawn Peters: Yeah, my team has had an interest in working with them, but we've been doing it really outside of this.


00:09:47.000 --> 00:09:50.000 Shawn Peters: this work stream, and I think we would continue to do that.


00:09:52.000 --> 00:10:05.000 BEL - 1 way vs. 2 way door: Okay, so my vote is just pause this from our standpoint, like, again, people should still get engaged with CBP. If, like, something starts going dramatically awry with experimentation, this is still a good group to talk about, and we can go exert pressure there. It's just not…


00:10:06.000 --> 00:10:07.000 BEL - 1 way vs. 2 way door: DI, so…


00:10:08.000 --> 00:10:13.000 BEL - 1 way vs. 2 way door: Okay. And then the ML one got killed a long time ago, so we don't need to talk about that.


00:10:13.000 --> 00:10:22.000 BEL - 1 way vs. 2 way door: Are we missing anything? I mean, I think this roughly captures AI enablement, like, all the big things we're all investing in right now, anyway, plus the kind of core systems that need to still survive.


00:10:22.000 --> 00:10:24.000 BEL - 1 way vs. 2 way door: Any gaps?


00:10:28.000 --> 00:10:35.000 BEL - 1 way vs. 2 way door: Okay. Um, I'll take these notes, and then I'll… I've already got Engin and I assigned action items. I'll need help from some others, too, on this.


00:10:35.000 --> 00:10:40.000 BEL - 1 way vs. 2 way door: I'll, uh, I'll come back with what I need from you. Um, and… and Jelly, or how do you pronounce your name?


00:10:39.000 --> 00:10:46.000 Angeli Kirk: Oh, yeah, sorry, I'm probably the random voice to chime in here. I'm not proposing that you, um…


00:10:43.000 --> 00:10:45.000 BEL - 1 way vs. 2 way door: Please, uh, please.


00:10:46.000 --> 00:10:59.000 Angeli Kirk: keep the… the experimentation group, but I will just say that it's increasingly on lead's radar that all of these increased diffs are not actually passing through to things like.


00:10:49.000 --> 00:10:51.000 BEL - 1 way vs. 2 way door: Yeah.


00:10:59.000 --> 00:11:03.000 Angeli Kirk: experiment shipped, and so I…


00:11:01.000 --> 00:11:03.000 BEL - 1 way vs. 2 way door: Yeah.


00:11:03.000 --> 00:11:10.000 Angeli Kirk: So just so that you know, that's sort of everyone's flag at the moment of something is not passing through to actual…


00:11:10.000 --> 00:11:18.000 Angeli Kirk: product value. Um, so if that could come back your way, just so that you kind of have your feelers up for it.


00:11:11.000 --> 00:11:13.000 BEL - 1 way vs. 2 way door: Yeah. Yeah.


00:11:15.000 --> 00:11:17.000 BEL - 1 way vs. 2 way door: Yeah.


00:11:18.000 --> 00:11:24.000 BEL - 1 way vs. 2 way door: I'll say, though, I don't think that's the fault of the experimentation platform. Like, it's not even getting there, like, there's a… there's a…


00:11:23.000 --> 00:11:32.000 Angeli Kirk: 100%, uh, 100%. I think now there's a bit more of, like, how do we think about all of the pipeline of, of…


00:11:24.000 --> 00:11:27.000 BEL - 1 way vs. 2 way door: Yeah, yeah.


00:11:32.000 --> 00:11:40.000 Angeli Kirk: each of the steps that it takes for something to make it all the way through to experimentation, so I suspect that there will be stones unturned on…


00:11:40.000 --> 00:11:48.000 Angeli Kirk: Each level, even if you might assume that we have incentivized something that is not passing things through to experimentation.


00:11:49.000 --> 00:11:51.000 BEL - 1 way vs. 2 way door: Uh, Tracy?


00:11:50.000 --> 00:12:12.000 traciecheung: Yeah, I was just gonna add to that, I can share in the Analytics Champions chat, but IG did an analysis into, kind of, like, whether they were seeing incremental impact from this AI-assisted diffs, and I think some of the… the net of it was, no, they're not seeing incremental impact or increased experimentation, and the thesis is that Edge is, like, tapped out from the constant context switching.


00:12:12.000 --> 00:12:20.000 traciecheung: There's, like, real issues within the actual process, like, the coding is not the bottleneck, it's the, like, process to get to experimentation, so…


00:12:20.000 --> 00:12:28.000 traciecheung: yeah, like, I think this… this kind of calls for, like, more deeper dive, but I'll… I'll share more details of that in our Champions group.


00:12:26.000 --> 00:12:28.000 BEL - 1 way vs. 2 way door: Yep.


00:12:28.000 --> 00:12:41.000 BEL - 1 way vs. 2 way door: I'll also say, if you follow Workplace, everybody's got their own AI framework, and it's like, okay. There's a lot of duplication going on that I think is of concern, which I think we'll have to settle out over time.


00:12:42.000 --> 00:12:49.000 BEL - 1 way vs. 2 way door: Okay, um, that's the easy topic, the harder topic, and I want to timebox us in.


00:12:50.000 --> 00:12:55.000 BEL - 1 way vs. 2 way door: less than 10 minutes, because then I want Tracy to have time. What does this group become?


00:12:56.000 --> 00:13:00.000 BEL - 1 way vs. 2 way door: Um, I… here's my two cents.


00:13:00.000 --> 00:13:06.000 BEL - 1 way vs. 2 way door: I think the pace of, at least, like, the way things are going in terms of, like, AI-native workflows.


00:13:07.000 --> 00:13:13.000 BEL - 1 way vs. 2 way door: I don't know that… I think the sneakers have a clear role to play, which is, like, being close to the work and having an opinion.


00:13:13.000 --> 00:13:16.000 BEL - 1 way vs. 2 way door: Um, I think the sort of…


00:13:16.000 --> 00:13:25.000 BEL - 1 way vs. 2 way door: every 6-month cadence of feedback that we built this around is not the right cadence, not the only right cadence anymore, although I still have always found value in, like.


00:13:25.000 --> 00:13:34.000 BEL - 1 way vs. 2 way door: getting together and talking about what are the big problems. I think that's valuable, but I think any feedback mechanism had to be much closer to the action than sort of, like.


00:13:34.000 --> 00:13:40.000 BEL - 1 way vs. 2 way door: kind of slower. And so, our original mission was to be that feedback loop, and I think that that's probably.


00:13:40.000 --> 00:13:44.000 BEL - 1 way vs. 2 way door: somewhat obfiated by AI, and we should do something else.


00:13:44.000 --> 00:13:47.000 BEL - 1 way vs. 2 way door: Vibha, you have a lot of thoughts on this, I'd love to hear yours.


00:13:47.000 --> 00:13:50.000 Vibha Virmani: I, I, I agree, this, this group is…


00:13:50.000 --> 00:13:55.000 Vibha Virmani: We have set up the processes, it's gone with AI, the things have changed, I…


00:13:55.000 --> 00:14:01.000 Vibha Virmani: I don't see a clear value proposition of this group existence, but having said that.


00:14:01.000 --> 00:14:13.000 Vibha Virmani: Uh, if we… if we move out of this, we need to make sure that how we have set up the SME group, there is a… there is a communication channel where, like, there were issues before that.


00:14:13.000 --> 00:14:18.000 Vibha Virmani: How does those each of the SME group come up with the roadmap? Is that aligned across?


00:14:18.000 --> 00:14:25.000 Vibha Virmani: Those kind of processes will have to be set up, because I don't want to go to a prior place where.


00:14:26.000 --> 00:14:34.000 Vibha Virmani: which, with AI is even worse, is, like, DI is doing whatever they feel like they have a value add, uh, SME groups are, like, creating because.


00:14:34.000 --> 00:14:48.000 Vibha Virmani: everybody's saying, uh, fuzziness on the boundaries, we are coding ourselves, uh, adding the diffs on the product, and all those things. It can go wild, wild west also, so we need to come up with some processes on those lines.


00:14:48.000 --> 00:14:52.000 Vibha Virmani: Um, and if we can land those, that would be okay.


00:14:53.000 --> 00:15:02.000 BEL - 1 way vs. 2 way door: Yeah, I mean, if you can see this group as being accountable for making sure we got the right folks in SME groups and that, like, a backstop for when things aren't going well, I'm okay with that. Like, I also think there's value in us.


00:15:03.000 --> 00:15:10.000 BEL - 1 way vs. 2 way door: as a channel for, hey, how are you dealing with this? Like, I think, like, we've… this has been a good group of people talk through things.


00:15:10.000 --> 00:15:23.000 BEL - 1 way vs. 2 way door: And we've done that, and that's not, like, a, you know, some big formal role, but it's still a useful communication channel where you may not, like, our leads don't talk to each other as much. I know my VP doesn't talk to anybody, um, so, like, you know, it's useful for me in that way, so…


00:15:25.000 --> 00:15:26.000 BEL - 1 way vs. 2 way door: Uh, Tracy?


00:15:26.000 --> 00:15:33.000 traciecheung: Yeah, I was gonna add that this forum has been useful, and I wonder if it's something where maybe we don't kill it, but we have, like, a less frequent.


00:15:33.000 --> 00:15:43.000 traciecheung: um, less frequent basis. And then also, I think we do have other things, like the quarterly business review and planning and roadmap things that are kind of, like, will keep us on track, too, so…


00:15:43.000 --> 00:15:44.000 BEL - 1 way vs. 2 way door: Yep.


00:15:43.000 --> 00:15:49.000 traciecheung: We could kind of test both, like, we have those forums in place, and then decrease the frequency of this meeting.


00:15:49.000 --> 00:15:57.000 BEL - 1 way vs. 2 way door: Yeah, okay. Um, one thing I will say, we did… we tried this out, and I don't want to do it again, is DI coming in here and telling us to do things.


00:15:57.000 --> 00:16:03.000 BEL - 1 way vs. 2 way door: that didn't work, won't work. Like, it wasn't you, Tracy. It was before you were here, so…


00:16:02.000 --> 00:16:04.000 traciecheung: I was like, okay. Yeah, cool.


00:16:03.000 --> 00:16:08.000 BEL - 1 way vs. 2 way door: Yeah, we're not gonna do that, so that's explicitly a non-goal, so…


00:16:09.000 --> 00:16:17.000 BEL - 1 way vs. 2 way door: Okay, I will write something on that and circulate another rev on this, and then we can go back through another set of comments and then gratify it, so…


00:16:17.000 --> 00:16:21.000 BEL - 1 way vs. 2 way door: Okay, uh, Tracy, you're up.


00:16:20.000 --> 00:16:25.000 traciecheung: Awesome. I'm gonna have, um, so Angeli leads the, um, the UXR team.


00:16:25.000 --> 00:16:34.000 traciecheung: And, um, she's got Megan on the line, too. Um, Angeli, do you want to… you set some context and then kick it off? Because I think you're… you're really close to this.


00:16:35.000 --> 00:16:40.000 Angeli Kirk: Thanks, and I'm joining in multiple places so that it's easier for me to share…


00:16:41.000 --> 00:16:47.000 Angeli Kirk: the deck, um, but if you heard all hands, um…


00:16:47.000 --> 00:16:53.000 Angeli Kirk: yesterday, I think, uh, Brady called out sort of the very top line results, um…


00:16:54.000 --> 00:17:00.000 Angeli Kirk: I wish you were having Nicole share these, but today is her last day, um…


00:17:00.000 --> 00:17:03.000 Angeli Kirk: Let me pull up… let me know if you can see this.


00:17:04.000 --> 00:17:06.000 Narendra Kambam: Yeah.


00:17:05.000 --> 00:17:17.000 Angeli Kirk: Can you see that? Okay. Um, but yeah, basically, we've pulled together the report for the overall DataX results, um.


00:17:17.000 --> 00:17:24.000 Angeli Kirk: Thank you to this group for the various ways that you've leaned in for participation, design, etc.


00:17:25.000 --> 00:17:27.000 Angeli Kirk: But, um…


00:17:28.000 --> 00:17:34.000 Angeli Kirk: Maybe I'll just jump to some of the core… the core findings. If nothing else.


00:17:34.000 --> 00:17:46.000 Angeli Kirk: I want you to see this slide, um, which has our efficiency metrics, which is sort of the perceived ease of making progress and the tooling satisfaction.


00:17:47.000 --> 00:17:51.000 Angeli Kirk: wave over wave. Uh, we went from…


00:17:51.000 --> 00:17:56.000 Angeli Kirk: Like, 38% on the efficiency up to 53%, so 15% gain.


00:17:56.000 --> 00:18:15.000 Angeli Kirk: there, and a 19% gain on tooling satisfaction. Uh, this is so striking of a result that we sort of paused, paced for a little bit, and then figured out what we needed to test, because in a really good wave-over-wave change, we would see, like, one percentage point.


00:18:15.000 --> 00:18:31.000 Angeli Kirk: Um, if something pretty big happens, it might be 5 percentage points. And so, we do think this is robust, um, but it's striking that it seems like we really captured that last wave was just as our AI tools and.


00:18:31.000 --> 00:18:39.000 Angeli Kirk: And products were starting to come out, and then the past 6 months have just been kind of an unprecedented.


00:18:39.000 --> 00:18:50.000 Angeli Kirk: set of changes, both in the tooling investments and, you know, analytics agent and… and DataMate, and then, you know, even actually over the course of the week when, um.


00:18:51.000 --> 00:18:56.000 Angeli Kirk: the survey was fielding, Claude Code was becoming more available to everyone. So, I think.


00:18:56.000 --> 00:19:04.000 Angeli Kirk: we don't need to spend more time here, but this is sort of a surprising jump in satisfaction, and I think everything else we can take.


00:19:04.000 --> 00:19:06.000 Angeli Kirk: is that…


00:19:06.000 --> 00:19:15.000 Angeli Kirk: there is this sense of, wait a minute, there is a lot that has changed in my workflow, and a lot of things that I was doing before are easier than they were.


00:19:15.000 --> 00:19:25.000 Angeli Kirk: Before, um, you have access to this deck, too, so part of what I want to do is give you a little bit of a tour of the structure, so that you can dig in where you want, but Tony, go ahead.


00:19:26.000 --> 00:19:35.000 BEL - 1 way vs. 2 way door: Uh, first off, this is great. I've got to kind of ran through the deck as well, like, I mean, amazing, like, great insights. I think… I have two thoughts. One, this is the result of strategy paying off.


00:19:35.000 --> 00:19:41.000 BEL - 1 way vs. 2 way door: So, like, good job, data infra. I also expect a regression next time, because of the explosion of new things.


00:19:41.000 --> 00:19:45.000 BEL - 1 way vs. 2 way door: And so, like, I don't know, you probably want to think about setting expectations on that.


00:19:45.000 --> 00:19:56.000 Angeli Kirk: Yeah, I have been sweating this. It's really hard to say what would happen next time, because both, like, all of the things that feel faster now and right now.


00:19:56.000 --> 00:20:02.000 Angeli Kirk: Capacity and tokens seem to be fairly unlimited by comparison to what we might expect.


00:20:02.000 --> 00:20:08.000 Angeli Kirk: If, um, leadership puts more efficiency measures and restrictions in. I think also.


00:20:08.000 --> 00:20:15.000 Angeli Kirk: there's so much more you can do than 6 months ago that that feels like this kind of AI mania to me, and I think.


00:20:15.000 --> 00:20:27.000 Angeli Kirk: what you can do today is going to now feel like, well, I should be able to do that. And so then… to your point, I think that we may expect some regression here, unless we find that the gains in the next 6 months are, like.


00:20:27.000 --> 00:20:36.000 Angeli Kirk: major model improvements or some of these other things, but, um, I fully agree that there is a risk here that some of this is.


00:20:28.000 --> 00:20:30.000 BEL - 1 way vs. 2 way door: Yep.


00:20:37.000 --> 00:20:42.000 Angeli Kirk: people responding based on their expectations of what it would be, and I think this.


00:20:42.000 --> 00:20:44.000 BEL - 1 way vs. 2 way door: Yeah.


00:20:42.000 --> 00:20:49.000 Angeli Kirk: change over the past 6 months has been a big delight, um, with still a lot of pain points. Go ahead.


00:20:47.000 --> 00:20:49.000 BEL - 1 way vs. 2 way door: Well, I'll send them.


00:20:49.000 --> 00:21:05.000 BEL - 1 way vs. 2 way door: I'll say real quick, the thing, like, I work a lot on the data access friction part, which is, you know, it's fallen from the top pain point to the second pain point in some of these things, but it's still there. Um, and I'm just seeing, like, we solved a bunch of data access friction problems last year, and now we're discovering a bunch of new ones because agents are doing new things.


00:21:05.000 --> 00:21:12.000 BEL - 1 way vs. 2 way door: And I think there will be a parent… that will be a general paradigm we'll find, which is we're effectively going to invent new pain points for ourselves.


00:21:12.000 --> 00:21:19.000 BEL - 1 way vs. 2 way door: Um, and I don't… I don't think… and we shouldn't blame data for that, right? It's like, this is just the game, you know? So…


00:21:13.000 --> 00:21:15.000 Angeli Kirk: Absolutely.


00:21:19.000 --> 00:21:24.000 Angeli Kirk: I think that's… I think that's right. So, both the shift in expectations and…


00:21:25.000 --> 00:21:30.000 Angeli Kirk: New challenges, and to your point, nobody was talking about context bloat.


00:21:30.000 --> 00:21:39.000 Angeli Kirk: This time, uh, 6 months ago, right? It was still trying to figure out, like, what is a skill, and how do I use this? And now it's which of the sea of…


00:21:39.000 --> 00:21:45.000 Angeli Kirk: of skills should I use, and how do I stop my system from slowing down? And so, um…


00:21:46.000 --> 00:21:52.000 Angeli Kirk: I do think… thank you for sort of bringing that sort of expectation along as we go, of just…


00:21:53.000 --> 00:22:03.000 Angeli Kirk: this is going to be, um, a continued ride, and I think we should celebrate the wins here, and the way that we frame this is a lot has really improved.


00:22:03.000 --> 00:22:13.000 Angeli Kirk: Now, let's also focus on the next set of hurdles and the remaining set of… or new set of pain points. So if you feel a tension here, like, wait a minute, you're telling me a lot of things have improved.


00:22:13.000 --> 00:22:24.000 Angeli Kirk: And you're emphasizing a lot of problems. Yes, if you feel that tension, I think we've done our job here of sort of the hunger on the next part of the journey.


00:22:25.000 --> 00:22:35.000 Angeli Kirk: But you will see in here, um, we had a section based on investments on what we were trying to use AI for, how, um…


00:22:36.000 --> 00:22:41.000 Angeli Kirk: How much benefit are you getting from AI on these different jobs?


00:22:41.000 --> 00:22:47.000 Angeli Kirk: And, um, I'm actually just gonna click there in the results. Everything, nearly everything jumped.


00:22:49.000 --> 00:22:51.000 Angeli Kirk: This was not the right…


00:22:52.000 --> 00:22:57.000 Angeli Kirk: Actually, I will start you here. Um, 4DE and…


00:22:58.000 --> 00:23:07.000 Angeli Kirk: and DS. We went through both the workflows, and then specific questions on, did AI help you do these things? And so you'll see that, actually.


00:23:07.000 --> 00:23:13.000 Angeli Kirk: For nearly everything, we got some good bumps within the workflows.


00:23:13.000 --> 00:23:20.000 Angeli Kirk: Uh, understand business context, um, probably had the least. It was also the most vague question. Um, but I do think that.


00:23:20.000 --> 00:23:31.000 Angeli Kirk: we are both getting better search and better documentation, and also a deluge of new content coming through, and so, you know, we'll need to keep digging there.


00:23:31.000 --> 00:23:38.000 Angeli Kirk: you'll see massive gains on finding the data you need and exploring data, and I think that really points to a lot of the investments.


00:23:39.000 --> 00:23:48.000 Angeli Kirk: we've made, and AI being able to help us actually search for data sources, um, and be able to do a lot of that, um, initial analysis, sort of.


00:23:49.000 --> 00:23:54.000 Angeli Kirk: some of this aligns with DataMate and Analytics Agent, but there's a whole suite of things that are now feeding in.


00:23:54.000 --> 00:23:56.000 Angeli Kirk: Here, um…


00:23:56.000 --> 00:24:03.000 Angeli Kirk: Logging has some improvement, but actually a little bit less than some of the others, and…


00:24:03.000 --> 00:24:13.000 Angeli Kirk: Um, we see notes about Falco and some other improvements, but it is a space that we see a little bit less AI being leveraged so far.


00:24:13.000 --> 00:24:26.000 Angeli Kirk: Um, you see author pipelines and metrics, like the bread and butter of DE, is all the way up to 92%, which we weren't even sure if that was a rating that could be possible with, um, with our populations.


00:24:26.000 --> 00:24:30.000 Angeli Kirk: Uh, dashboarding is… oh, go ahead. Yeah, please.


00:24:27.000 --> 00:24:30.000 Narendra Kambam: Can I ask a question?


00:24:30.000 --> 00:24:41.000 Narendra Kambam: Um, Julie, so it says 81% from last year, and I believe people still were using, like, an ADMate or dev mate to, um, push.


00:24:41.000 --> 00:24:45.000 Narendra Kambam: you know, data storm pipelines. Um…


00:24:45.000 --> 00:24:48.000 Narendra Kambam: What does this tell us? That means that.


00:24:48.000 --> 00:24:55.000 Narendra Kambam: They can create more pipelines now, better than last, you know, quarter. More…


00:24:55.000 --> 00:24:58.000 Narendra Kambam: easily. Um…


00:24:58.000 --> 00:25:04.000 Angeli Kirk: Yeah, and Megan, I want you to jump in at any point. Megan, um, helped do a lot of the open-end analysis.


00:25:04.000 --> 00:25:10.000 Angeli Kirk: But what we're hearing through a lot of these things across spaces is that it can be a mix of.


00:25:11.000 --> 00:25:17.000 Angeli Kirk: I can do this thing faster than I could do before. When someone is less expert, we're finding people say, I can do.


00:25:17.000 --> 00:25:23.000 Angeli Kirk: some new things that I couldn't do before, but actually, often we're finding people who are expert.


00:25:23.000 --> 00:25:37.000 Angeli Kirk: already expert, look at it and go, oh, I put this through, and actually I see enough that's reasonable that either it's a great start and I can tweak it, or I have enough expertise to know that this actually looks quite good, and it's saving me a lot of time.


00:25:37.000 --> 00:25:43.000 Angeli Kirk: Um, these tend… tend to be what we're… we're seeing. Um, we also hear themes about.


00:25:43.000 --> 00:25:52.000 Angeli Kirk: Setting up tests can be a lot faster this way, and in some cases, you can even, like, set up the test before you ask it to generate the pipeline so it can keep it on track.


00:25:53.000 --> 00:25:58.000 Narendra Kambam: Got it. I think it would be fantastic to see, I mean, I can… I can look at it, too.


00:25:58.000 --> 00:26:10.000 Narendra Kambam: uh, would be good to compare this against, um, like, the metrics, like Dataswarm DDM and agent-assisted DataSwarm diff, and to see if there is a good, you know, correlation there, you know, between.


00:26:11.000 --> 00:26:14.000 Narendra Kambam: The dissatisfaction versus the output.


00:26:13.000 --> 00:26:22.000 Angeli Kirk: I love that. I could use a little bit of help here, because I just lost a chunk of my quant.


00:26:22.000 --> 00:26:33.000 Angeli Kirk: capacity at the moment, but I do think increasingly, where I think some of our next steps can go is the more that we can connect this to the log data, where we either see that.


00:26:32.000 --> 00:26:34.000 Narendra Kambam: Yeah.


00:26:33.000 --> 00:26:44.000 Angeli Kirk: Both the sentiment and the log data are moving together, and that gives us, you know, we can keep following the log data in between the sessions, or we see a gap, and that gives us a clue that we should be digging in.


00:26:38.000 --> 00:26:40.000 Narendra Kambam: There.


00:26:44.000 --> 00:26:50.000 Angeli Kirk: deeper to understand what's going on. Um, I think that that's…


00:26:50.000 --> 00:26:53.000 Angeli Kirk: Would be a really helpful way to understand these more.


00:26:55.000 --> 00:27:02.000 Angeli Kirk: Um, yeah. Dashboarding, we still see as low, although it has increased.


00:26:55.000 --> 00:26:57.000 Narendra Kambam: I'm good, yeah, please.


00:27:02.000 --> 00:27:05.000 Angeli Kirk: We do get a lot of comments in there.


00:27:05.000 --> 00:27:15.000 Angeli Kirk: Megan, disagree again if I got this wrong, that are a bit, sort of, in the Unidash is… is dead because I'm using all of these, like, Nest apps, or, you know.


00:27:15.000 --> 00:27:26.000 Angeli Kirk: self-serving in other ways. Um, I suspect that that's both a benefit and also a how on earth do we think about governance or tracking of.


00:27:26.000 --> 00:27:31.000 Angeli Kirk: All these other things proliferating, and so maybe just a flag there that.


00:27:31.000 --> 00:27:36.000 Angeli Kirk: it's a place that we should continue keeping an eye on and investing in, but to Tony's point about.


00:27:37.000 --> 00:27:42.000 Angeli Kirk: New advances also opening up new challenges. We'll want to pay attention there.


00:27:40.000 --> 00:27:42.000 BEL - 1 way vs. 2 way door: Yeah.


00:27:42.000 --> 00:27:45.000 BEL - 1 way vs. 2 way door: Although, I bet you that one's gonna go away up next time.


00:27:45.000 --> 00:27:53.000 BEL - 1 way vs. 2 way door: I just… I mean, the experience of Nest is so dramatically better. Um, I bet everyone… because Unitash was a big drag on all this, and I think…


00:27:53.000 --> 00:27:58.000 BEL - 1 way vs. 2 way door: you're right, new things will come up, but I think everybody loves the tooling now.


00:27:57.000 --> 00:28:01.000 Angeli Kirk: Awesome. Yeah, so we'll… we'll… go ahead.


00:27:58.000 --> 00:28:03.000 Megan Farwell: Yeah, I will say Unidash gets pretty, uh, resoundingly…


00:28:04.000 --> 00:28:13.000 Megan Farwell: criticized in the open ends, kind of across areas, so I would also expect that as people adopt different tooling, that they will… we will see the score boost.


00:28:13.000 --> 00:28:22.000 Angeli Kirk: Um, and I'm hearing a lot of delight about Nest so far, sort of both things in the survey, but just in general, where we're hearing some.


00:28:22.000 --> 00:28:24.000 Angeli Kirk: Brave results there. And then…


00:28:25.000 --> 00:28:30.000 Angeli Kirk: We also saw some gains for the data operations and support. Um…


00:28:30.000 --> 00:28:36.000 Angeli Kirk: And some of these… I suspect that some data operations and some of the authoring pipelines.


00:28:36.000 --> 00:28:43.000 Angeli Kirk: To the point about, you know, we had DevMate before in some of these things, there actually may have been some boost already.


00:28:43.000 --> 00:28:50.000 Angeli Kirk: um, last wave, um, but I think, you know, especially this Find the Data and Explore Data have really.


00:28:50.000 --> 00:28:55.000 Angeli Kirk: really jumped in the interim. Um, just so you see it, the slide after it.


00:28:55.000 --> 00:29:10.000 Angeli Kirk: We'll give some more, um, themes from the open ends about the kinds of comments that we have in terms of what may have driven there. Uh, we've tried to use, sort of, how common some of these comments are to surface that there, but it's not.


00:29:10.000 --> 00:29:16.000 Angeli Kirk: Statistical in terms of, um, this comment came up this, you know, this percent of time.


00:29:18.000 --> 00:29:23.000 Angeli Kirk: And so that's probably one place that you'll want to take a little more of a look. Um…


00:29:24.000 --> 00:29:30.000 Angeli Kirk: We also just showed what happens if we only look at the repeat responders. I won't spend time there, but just as our robustness check.


00:29:30.000 --> 00:29:37.000 Angeli Kirk: Um, versus, sort of, the full sample. Um, and then similarly, you can see for DS.


00:29:37.000 --> 00:29:48.000 Angeli Kirk: we got a lot of big gains in the finding data, exploring data, um, and even bigger gain on the finding data. They were lower before, but I suspect that DEs, in some cases, may have a.


00:29:48.000 --> 00:29:54.000 Angeli Kirk: Better baseline knowledge of what data exists where, and so, like, this may be helping them.


00:29:54.000 --> 00:29:58.000 Angeli Kirk: Close the gap to some extent. Um…


00:29:59.000 --> 00:30:07.000 Angeli Kirk: And again, you know, conduct state analysis went up, but all of the things went up, and that's sort of the overall activity.


00:30:07.000 --> 00:30:12.000 Angeli Kirk: I, um… let's see, let me show you… this one is… this is specifically…


00:30:12.000 --> 00:30:17.000 Angeli Kirk: Items that we chose last time around where we were investing in AI support.


00:30:17.000 --> 00:30:25.000 Angeli Kirk: And so, I find this set of results a bit shocking, um, but you can see here that.


00:30:26.000 --> 00:30:31.000 Angeli Kirk: If we just asked people who said a great deal or a lot of progress.


00:30:31.000 --> 00:30:37.000 Angeli Kirk: Um, like, the percent of people who put authoring queries, that was 44 percentage point increase.


00:30:37.000 --> 00:30:44.000 Angeli Kirk: Um, I just… this is not normal, so please, please don't expect this in the future. It's likely to go the other direction. Um…


00:30:45.000 --> 00:30:56.000 Angeli Kirk: Uh, but you can see, I mean, every single one that we asked about has increased. Um, and then maybe the other theme that I'll call out is, I think some of the more straightforward work.


00:30:56.000 --> 00:31:03.000 Angeli Kirk: So the queries, the, you know, exploratory analysis, the pipelines, um…


00:31:03.000 --> 00:31:13.000 Angeli Kirk: the things that are more code-based, those really had the biggest jumps, and then as you go down, the ones that had lower gains, um, do tend to be more complex work.


00:31:13.000 --> 00:31:21.000 Angeli Kirk: So, the understanding best practices, the identifying the key insights, the reporting, that those… those…


00:31:21.000 --> 00:31:32.000 Angeli Kirk: still tend to take more judgment and more craft, I would say, and so those have grown, but not in the same way of things that can actually be a bit more code, like, anchored in code.


00:31:33.000 --> 00:31:36.000 Angeli Kirk: Any questions or thoughts on this one?


00:31:37.000 --> 00:31:46.000 BEL - 1 way vs. 2 way door: I'll just say what… what you just said. I mean, this has been amazing, like, truly, like, I can look at this and see it in my own work. Um, I do expect some regression to the need on some of these things.


00:31:47.000 --> 00:31:55.000 BEL - 1 way vs. 2 way door: Um, and then, yeah, I mean, the other thing I take from this is, like, everybody's worried that AI's gonna take their jobs. To your point, that bottom bit is our jobs.


00:31:55.000 --> 00:31:59.000 BEL - 1 way vs. 2 way door: So, you know, hooray, we still have jobs.


00:31:59.000 --> 00:32:03.000 Angeli Kirk: It's true. The thing I will say that I worry about…


00:32:03.000 --> 00:32:15.000 Angeli Kirk: I will say in this… with this audience, is just given some of the language from leadership, I'm hoping that the nuance here about how the things that require more judgment.


00:32:16.000 --> 00:32:23.000 Angeli Kirk: And more craft, and more, like, that actually can distinguish, like, what's slop versus, like, the thing that you really need.


00:32:23.000 --> 00:32:28.000 Angeli Kirk: to make good decisions. I'm hoping that we can protect enough.


00:32:28.000 --> 00:32:41.000 Angeli Kirk: respect and understanding of what that gives us, um, sort of in… in the rush for volume and speed, but I think you're right, like, this is the place that we can really lean in with our expertise and…


00:32:41.000 --> 00:32:43.000 Angeli Kirk: And the experience that we've had.


00:32:43.000 --> 00:32:53.000 BEL - 1 way vs. 2 way door: My VP asked me, like, what percent of our jobs do you think gets replaced by AI? And I'm like, it's not more than 40%, I don't think. There is a percent, which is, like, up in that top bit, which is, like.


00:32:53.000 --> 00:32:58.000 BEL - 1 way vs. 2 way door: Like, kind of, like, work that, you know, wasn't the fun bit of what we did, and yes, that's helped by it.


00:32:58.000 --> 00:33:02.000 BEL - 1 way vs. 2 way door: But the thinking bit is still important, so… anyway.


00:33:01.000 --> 00:33:04.000 Angeli Kirk: Yeah. Megan?


00:33:04.000 --> 00:33:13.000 Megan Farwell: Yeah, I will say, and I don't remember which slide it's on, one of the, um, bits of feedback we got was that people said they felt like it was harder to get their work.


00:33:13.000 --> 00:33:25.000 Megan Farwell: seen and shown because there was such volume from everybody else sort of putting things out there. So yeah, there's… there's the thinking bit that needs to go into it, but there's also this sort of counterbalance of, like.


00:33:25.000 --> 00:33:32.000 Megan Farwell: It's sometimes difficult to say, like, this is the high-quality work and distinguish it from everything else, so that's what gets actioned on.


00:33:32.000 --> 00:33:35.000 BEL - 1 way vs. 2 way door: Well, and that's gonna be a growing, like…


00:33:35.000 --> 00:33:41.000 BEL - 1 way vs. 2 way door: Theme of analytics here, which is, like, okay, finding data is trivial now.


00:33:41.000 --> 00:33:54.000 BEL - 1 way vs. 2 way door: is it the right data? It's always been a problem, but it used to be you go talk to your DS. Now it's like, well, the machine told me this thing. I mean, I'm saying this in practice, the rest of you probably are too. It's… it's not good, and so this is where, to me, our.


00:33:54.000 --> 00:34:01.000 BEL - 1 way vs. 2 way door: The infrastructure strategy part of it has to go, which is, like, enabling good governance of this so that the right things can stand out.


00:34:01.000 --> 00:34:05.000 BEL - 1 way vs. 2 way door: And it is, I'm not saying it isn't, we're putting tremendous, you know, effort into that, so…


00:34:06.000 --> 00:34:12.000 Angeli Kirk: Yeah, I know we are really short on time. I have a little extra time, but I realize we only booked a little bit.


00:34:13.000 --> 00:34:24.000 Angeli Kirk: Um, more from here, but just a flag that, um, we had thrown in a question that were sort of, what were the top pain points that were circulating among leads, and sort of in the discussion of the community.


00:34:24.000 --> 00:34:33.000 Angeli Kirk: every single one of those has decreased, although some more than others. Um, like, the friction around access and privacy has certainly.


00:34:33.000 --> 00:34:38.000 Angeli Kirk: improved… so, and these, the smaller number is better, um…


00:34:38.000 --> 00:34:50.000 Angeli Kirk: capacity, you know, documentation, all of those have been improved. There are still some that have been, you know, benefited less, I think, around, like, on-call rotations and some of this, but…


00:34:50.000 --> 00:35:04.000 Angeli Kirk: Um, at least at the moment, I think we're seeing big improvements. We should decide, I think, if we run this survey again, whether there are new pain points that we'd like to emphasize, especially ones that come up.


00:35:04.000 --> 00:35:16.000 Angeli Kirk: because of AI, so this, you know, finding signal in the noise, the sort of ensuring… being able to determine that something is quality versus not, um…


00:35:16.000 --> 00:35:29.000 Angeli Kirk: If we end up with more restrictions on tokens or capacity, some of… we've got capacity in here, but this time around, we kept it the same to see what we could see on the changes, but…


00:35:30.000 --> 00:35:35.000 Angeli Kirk: My hunch is that top pain points will have shifted as we go.


00:35:36.000 --> 00:35:38.000 BEL - 1 way vs. 2 way door: Yeah, agreed.


00:35:38.000 --> 00:35:40.000 Angeli Kirk: Um, and then I…


00:35:40.000 --> 00:35:46.000 Angeli Kirk: We'll leave the rest for you to look at. We do have some sections that focus on the open-end analysis.


00:35:46.000 --> 00:35:49.000 Angeli Kirk: And, oh, sorry, Steve, go ahead.


00:35:48.000 --> 00:35:53.000 Steve Fischer: I was just gonna ask, is this okay to share, like, with our teams, or with… what's…


00:35:52.000 --> 00:36:03.000 Angeli Kirk: Yes, this, this is. So, um, your VPs already have access. Um, this is shareable, and then by the end of the week, Nick.


00:36:03.000 --> 00:36:16.000 Angeli Kirk: should be putting out, um, the general post, but all of this information we feel comfortable with at this point, so please feel free to dig in. Um, you have access to the data with a business reason.


00:36:16.000 --> 00:36:26.000 Angeli Kirk: As long as we do the people data training, and even if we can't do that analysis, would love to kind of consult on any places where we might be able to help you.


00:36:26.000 --> 00:36:30.000 Angeli Kirk: Look on the right… right places. Um…


00:36:28.000 --> 00:36:31.000 Steve Fischer: Okay. Yeah.


00:36:30.000 --> 00:36:35.000 Angeli Kirk: And then a couple of themes on the open ends that you will see a good bit of are kind of distrust of…


00:36:35.000 --> 00:36:41.000 Angeli Kirk: Quality, output, etc, and sort of the continued hallucination that even if they're less, they'll probably.


00:36:41.000 --> 00:36:44.000 Angeli Kirk: continue to be a pain. Um…


00:36:44.000 --> 00:36:49.000 Angeli Kirk: Anyway, I'll stop there, but I interrupted, I think, Stevie, you were going to say something else.


00:36:48.000 --> 00:36:54.000 Steve Fischer: Oh, I was just gonna ask, and then if we have follow-up questions or if our teams have, can we ping you directly?


00:36:54.000 --> 00:37:07.000 Angeli Kirk: Absolutely. Um, ideally ping Megan and me together, but feel free, either way, um, we can dig in. And we have kind of this shorter version of the report, and then the full, full appendix.


00:36:55.000 --> 00:36:56.000 Steve Fischer: Yeah.


00:36:59.000 --> 00:37:01.000 Steve Fischer: Okay. Yeah.


00:37:07.000 --> 00:37:19.000 Angeli Kirk: Because we find that, actually, we already know, we've got a lot of questions on very, you know, specific items that are in there, and there's a lot of nuggets, um, for everyone, so do please reach out.


00:37:19.000 --> 00:37:24.000 Angeli Kirk: Um, feel free to comment in the deck, it's, it's, you know, any, anything is open.


00:37:25.000 --> 00:37:33.000 Angeli Kirk: There, um, and we'd love to hear back of sort of what either feels interesting, surprising, or useful as well, because it helps us tweak as we go.


00:37:32.000 --> 00:37:35.000 Steve Fischer: Yeah. Great work. Thank you.


00:37:35.000 --> 00:37:37.000 BEL - 1 way vs. 2 way door: Super useful, yeah, thank you.


00:37:37.000 --> 00:37:49.000 Angeli Kirk: Thank you. It's… it has been a lot, but the community really came together to even just to show up and take it. Um, of the FTEs, analytics gave us the best response rates, which.


00:37:49.000 --> 00:37:54.000 Angeli Kirk: actually lets us get these numbers and get the themes, and so I…


00:37:54.000 --> 00:37:59.000 Angeli Kirk: Um, we're really grateful for all the support that went into making this to come together.


00:38:01.000 --> 00:38:03.000 BEL - 1 way vs. 2 way door: Cool. Alright, thanks, y'all.


00:38:03.000 --> 00:38:05.000 Narendra Kambam: Thank you.


