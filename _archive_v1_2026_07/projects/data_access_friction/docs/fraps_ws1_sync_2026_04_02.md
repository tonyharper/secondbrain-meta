<!-- Source: https://docs.google.com/document/d/191yiFjSvOzvUiwcp5hpiZ0bj0hPBmrNe1mWdxeVhkHI/edit -->
# [w] FRAPS WS1 Sync - April 2, 2026, 10:05-10:30 AM PDT [AI meeting transcript by Zoom]

*AI Generated Document. Please note that this working copy of the transcribed meeting is AI-generated and is thus subject to error.  As this working document is subject to edits, it may not always accurately reflect the contents of the meeting.*


[*👉 Found an issue with AI meeting transcript? File a bug here. ✍️*](https://www.internalfb.com/butterfly/form/889746210506907?default_responses=%7B%22share%22%3A%22https%3A%5C%2F%5C%2Fdocs.google.com%5C%2Fdocument%5C%2Fd%5C%2F191yiFjSvOzvUiwcp5hpiZ0bj0hPBmrNe1mWdxeVhkHI%5C%2Fedit%3Ftab%3Dt.0%22%2C%22debug_info%22%3A%22zoom_meeting_id%3A+92397364549%22%7D)



Invitees: Wenlong Dong, Anisha Patel, Tola Dalton, Can Lin, George Schnabel, Rachel Lee, Tony Harper, Aaron Morris


00:00:13.000 --> 00:00:15.000 Anisha Patel: Good morning, Wenlong.


00:00:14.000 --> 00:00:16.000 Wenlong Dong: Good morning, Melissa.


00:00:20.000 --> 00:00:27.000 Anisha Patel: I wish this AI meeting notes can… can be fixed. It takes… it creates delays in people joining.


00:00:28.000 --> 00:00:33.000 Wenlong Dong: Does it work? I turned on AI notes last time and didn't get anything.


00:00:34.000 --> 00:00:36.000 Anisha Patel: Oh, you did not?


00:00:35.000 --> 00:00:37.000 Wenlong Dong: Right, I don't know why.


00:00:37.000 --> 00:00:42.000 Anisha Patel: It was… there was an issue last week, but they fixed it.


00:00:41.000 --> 00:00:44.000 Wenlong Dong: Oh, it's just yesterday. I don't know.


00:00:43.000 --> 00:00:46.000 Anisha Patel: Oh, is it? Interesting.


00:00:45.000 --> 00:00:47.000 Wenlong Dong: Yeah.


00:00:50.000 --> 00:00:57.000 Wenlong Dong: Yeah, this morning, Cloud Code just does everything better to me. It screwed up my documents.


00:00:50.000 --> 00:00:52.000 Anisha Patel: Okay.


00:00:58.000 --> 00:01:02.000 Wenlong Dong: I have to manually fix it.


00:00:58.000 --> 00:01:00.000 Can Lin: Oh.


00:01:03.000 --> 00:01:12.000 SEA - Sane: Uh, we have noticed that when we run our semantic model eval runners, uh, during certain parts of the day, it runs a lot worse. Claude is just dumber.


00:01:12.000 --> 00:01:15.000 SEA - Sane: during some parts of the day, we think it's because it's getting high utilization.


00:01:15.000 --> 00:01:17.000 Wenlong Dong: Oh, really.


00:01:17.000 --> 00:01:32.000 Can Lin: It may save some compute, and you… and also, I think the company, by default, changes the effort from high to medium, so sometimes you need to explicitly set it, otherwise it'll keep resetting to medium, so you need to be careful.


00:01:31.000 --> 00:01:33.000 SEA - Sane: Yeah.


00:01:32.000 --> 00:01:38.000 Anisha Patel: The funniest, the worst thing for me is, like, giving some prompts and noticing that my prompts got cropped.


00:01:39.000 --> 00:01:45.000 Anisha Patel: In its compression and then it comes up with something which I totally did not expect.


00:01:45.000 --> 00:01:47.000 Anisha Patel: And I'm still trying to figure out when this is happening.


00:01:49.000 --> 00:01:53.000 Anisha Patel: It kind of dropped some of the prompt criteria.


00:01:54.000 --> 00:01:56.000 Wenlong Dong: Yeah.


00:01:59.000 --> 00:02:04.000 Anisha Patel: I think we almost have a quorum. Let's wait for Rachel to join.


00:02:04.000 --> 00:02:07.000 Anisha Patel: Or maybe give it a minute and we get started.


00:02:07.000 --> 00:02:09.000 Wenlong Dong: Yeah.


00:02:09.000 --> 00:02:11.000 Anisha Patel: Um…


00:02:11.000 --> 00:02:13.000 Anisha Patel: No, I did the.


00:02:15.000 --> 00:02:27.000 Anisha Patel: I did the measurement discussion as one of the first topics to discuss. So again, thank you for sharing the dashboard. Just an FYI to those who haven't seen yet, the first version of the dashboard is ready.


00:02:27.000 --> 00:02:30.000 Anisha Patel: Feel free to review, provide your feedback and comments.


00:02:31.000 --> 00:02:41.000 Anisha Patel: Um, I think the idea is to use majority of the time to discuss our plan for measurement and how we want to approach forward. I will let, uh… Wenong, I'll pass it on to you, and…


00:02:42.000 --> 00:02:50.000 Wenlong Dong: Right, okay. I don't know how many of you have a… have a look at the… I tried to shrink it, it was too long.


00:02:50.000 --> 00:02:59.000 Wenlong Dong: Um, most of this is… was, of course, was written by, uh, agent, but I have a very good, like, a revision of that, but somehow.


00:02:59.000 --> 00:03:04.000 Wenlong Dong: It was screwed up by Claude, so I only have a… just a manually…


00:03:05.000 --> 00:03:12.000 Wenlong Dong: Updated document. I will fix that. I mean, anyway, this is just for discussion, right?


00:03:12.000 --> 00:03:17.000 Wenlong Dong: This is not for an actual proposal, even though I feel that, uh.


00:03:17.000 --> 00:03:24.000 Wenlong Dong: Uh, that, uh, that the agent does a good job to at least capture what I was thinking.


00:03:24.000 --> 00:03:27.000 Wenlong Dong: Uh, from the high level. Um…


00:03:27.000 --> 00:03:33.000 Wenlong Dong: So, I'll share that, I wanted, uh, like, uh, so, basically.


00:03:34.000 --> 00:03:39.000 Wenlong Dong: Anisha and I discussed initially that, hey, what is the work stream? How do we…


00:03:39.000 --> 00:03:51.000 Wenlong Dong: uh, like, come up with a strategy together and guide these different world streams, and how do we measure all this, right? I know that, uh, Tony has thought a lot about the measurement.


00:03:51.000 --> 00:03:59.000 Wenlong Dong: But, uh, how do we connect our strategy with the measurement? That's a… that's a question. Especially here, uh, basically.


00:04:00.000 --> 00:04:07.000 Wenlong Dong: First of all, among us, do we… do we have a good definition of aging of friction? What is… what that is?


00:04:07.000 --> 00:04:15.000 Wenlong Dong: And second is that how to rigorously measure it, and then, what is our prioritization framework?


00:04:15.000 --> 00:04:19.000 Wenlong Dong: Right? And then finally, what's our investment on the plan?


00:04:19.000 --> 00:04:24.000 Wenlong Dong: So, that's, uh… that's a… these are the key topics I wanted to see if…


00:04:25.000 --> 00:04:33.000 Wenlong Dong: Uh, if, uh, we can, like, the leads here can brainstorm and, and discuss about, uh, uh, these major topics.


00:04:34.000 --> 00:04:40.000 Wenlong Dong: But, um, I don't want to, like, make this to be too free-formed, so that's why I came up with this.


00:04:40.000 --> 00:04:46.000 Wenlong Dong: some initial thoughts, and then we can discuss that. I just want to quickly.


00:04:46.000 --> 00:04:53.000 Wenlong Dong: probably share 5 minutes about what I have done. I forget this context motivation, right? This is just a copy.


00:04:53.000 --> 00:04:56.000 Wenlong Dong: And then, what's the edge generation, uh…


00:04:57.000 --> 00:05:04.000 Wenlong Dong: So, I see that there are two different ways we think about this, and I chatted briefly with the can name.


00:05:04.000 --> 00:05:11.000 Wenlong Dong: Uh, there are two ways, ones that are, hey, interruption-based, but more given session, is it interrupted.


00:05:11.000 --> 00:05:16.000 Wenlong Dong: If it's interrupted, then, okay, this session hits some problem, right?


00:05:16.000 --> 00:05:22.000 Wenlong Dong: Uh, or you can purely say how many interruptions were hitting.


00:05:22.000 --> 00:05:31.000 Wenlong Dong: The other is the outcome-based. It does the… no matter how many failures happened, does the agent get the right outcome?


00:05:31.000 --> 00:05:38.000 Wenlong Dong: Uh, expected outcome, right? Uh, so these are, uh, two lenses there. So…


00:05:39.000 --> 00:05:51.000 Wenlong Dong: Uh, maybe we can discuss whether we should do one or two, but one has benefits that is simple and actionable and easy to measure, right? But anyway.


00:05:51.000 --> 00:05:56.000 Wenlong Dong: I just put… let me just quickly walk through what I am thinking here. Secondly, that.


00:05:56.000 --> 00:06:04.000 Wenlong Dong: the friction… now we know what the friction is. Let's say the sessions are interrupted, right, or…


00:06:04.000 --> 00:06:08.000 Wenlong Dong: Uh, agent doesn't do the right job. How do we…


00:06:08.000 --> 00:06:17.000 Wenlong Dong: uh, like, classify this, uh, friction. Um, so I try to use, like, dimensional model of the two dimensions. One is, uh.


00:06:17.000 --> 00:06:23.000 Wenlong Dong: friction category. So, yesterday, I asked the agent to.


00:06:23.000 --> 00:06:29.000 Wenlong Dong: to walk through, I think, uh, 50 or 60 different workplace groups.


00:06:29.000 --> 00:06:38.000 Wenlong Dong: And identify all the posts from those groups, and then categorize those into different buckets.


00:06:38.000 --> 00:06:43.000 Wenlong Dong: So this… I look at the categorization, seems to be…


00:06:43.000 --> 00:06:53.000 Wenlong Dong: Uh, pretty good. Initially, yes, before that, I just asked the agent to just read some docs.


00:06:53.000 --> 00:06:58.000 Wenlong Dong: And then that… those… that set of categories were really bad.


00:06:58.000 --> 00:07:03.000 Wenlong Dong: Uh, and there's only 2 categories will make sense. And now, after reading all the.


00:07:03.000 --> 00:07:08.000 Wenlong Dong: Uh, one… I think… how many… 130…


00:07:08.000 --> 00:07:15.000 Wenlong Dong: uh, posts, uh, reported by people, it came up with this, uh, this list of issues, right? You can see.


00:07:15.000 --> 00:07:18.000 Wenlong Dong: Identity issue.


00:07:18.000 --> 00:07:28.000 Wenlong Dong: data center TV issue, execution controls, permission prompts, network controls, and alcohol denials, and also allow list and grading, right? These are seven.


00:07:28.000 --> 00:07:35.000 Wenlong Dong: Categories, um, and also, it'll also, like, break down this percentage based on the posts.


00:07:35.000 --> 00:07:44.000 Wenlong Dong: And then we can also discuss whether this is the right list. And second category is about the list of agents.


00:07:44.000 --> 00:07:50.000 Wenlong Dong: Uh, this part, uh, I just took it from the… from the security, privacy.


00:07:50.000 --> 00:07:56.000 Wenlong Dong: uh, like, aligned, like, risk side aligned list, but I added a mid-SLI.


00:07:56.000 --> 00:07:58.000 Wenlong Dong: And later on, I found it out.


00:07:58.000 --> 00:08:07.000 Wenlong Dong: Uh, by looking at all this friction here, there's a different table. Unfortunately, the cloud screwed my dog, so…


00:08:07.000 --> 00:08:10.000 Wenlong Dong: I don't have this version here.


00:08:10.000 --> 00:08:15.000 Wenlong Dong: Okay, it's… this is better, right? It's different, right?


00:08:10.000 --> 00:08:12.000 SEA - Sane: Well…


00:08:15.000 --> 00:08:17.000 Wenlong Dong: Yeah, this is listening.


00:08:16.000 --> 00:08:21.000 SEA - Sane: Do you want comments… Wenlen, do you want comments and questions at the end of this, or as you go?


00:08:20.000 --> 00:08:32.000 Wenlong Dong: Yeah, yeah, just super quick, I just walk through what I have done, and then I just paused there. And then, this just, uh, just to show the thinking, right? So now, let's say we have two dimensions. One is, uh.


00:08:32.000 --> 00:08:42.000 Wenlong Dong: agent, the other is the friction category. Can we, like, start to say, hey, which bucket has most of the highest friction? Do we have the measurement? Do we have the data?


00:08:42.000 --> 00:08:54.000 Wenlong Dong: you know, can we, like, highlight which cells we want to focus on more to solve them, right? And then, who is going to solve each bucket, right?


00:08:54.000 --> 00:08:59.000 Wenlong Dong: Um, and then which Workstream can take the work? So that's…


00:08:59.000 --> 00:09:04.000 Wenlong Dong: Uh, that's the next step, once we have that. And then, of course, how to.


00:09:04.000 --> 00:09:09.000 Wenlong Dong: How to do the… you leverage the agent observability as a foundation to.


00:09:09.000 --> 00:09:15.000 Wenlong Dong: enable this, uh, like, measurement. And after that, we can start to talk about, uh.


00:09:15.000 --> 00:09:22.000 Wenlong Dong: Uh, like, uh, the investment in the plan. So this is just an overall thinking in my mind. Okay, I'll pause here.


00:09:23.000 --> 00:09:28.000 SEA - Sane: Um, couple comments. Uh, number… go back to… scroll down to your tables, please.


00:09:27.000 --> 00:09:30.000 Wenlong Dong: Oh, okay, okay, yeah. This one.


00:09:29.000 --> 00:09:39.000 SEA - Sane: Um, yeah, no, actually, go up to the first off, to the, uh, types of friction. What would something like, uh, policy zones block my test or run? Where would that fall?


00:09:40.000 --> 00:09:50.000 Wenlong Dong: Uh… good, uh, good question. So, let me see. First of all, this, this should be expandable, right? This lesson, uh…


00:09:49.000 --> 00:09:51.000 SEA - Sane: Yeah.


00:09:50.000 --> 00:09:53.000 Wenlong Dong: So…


00:09:53.000 --> 00:09:59.000 Wenlong Dong: So maybe, so far, the agent haven't… no one has reported this from agent's perspective.


00:09:59.000 --> 00:10:05.000 Wenlong Dong: Um, but I do see that there are a bunch of new guardrails are adding. So basically, we are…


00:10:05.000 --> 00:10:17.000 Wenlong Dong: we're chasing the other side of us. We know that there are two other world strengths in security and privacy, right? One is agent security, the other is agent privacy.


00:10:17.000 --> 00:10:20.000 Wenlong Dong: So, basically, they are our opposite.


00:10:20.000 --> 00:10:27.000 Wenlong Dong: They are adding new DRLs, and we are reducing the version. So, you know, we expect this to DRL.


00:10:24.000 --> 00:10:35.000 SEA - Sane: Yeah, okay. So, so maybe we're missing something, basically. We can add them as we get them. Okay, that's fine. Um, and then on the list of agents, um, I had my team do analysis, and I can share it.


00:10:29.000 --> 00:10:31.000 Wenlong Dong: Yes.


00:10:35.000 --> 00:10:41.000 SEA - Sane: About what we're seeing in the data on the agents, and so we can update this list based on what we're seeing in the data. I think that.


00:10:39.000 --> 00:10:41.000 Wenlong Dong: Yes.


00:10:41.000 --> 00:10:44.000 SEA - Sane: Like, it's really clear some of the, like…


00:10:44.000 --> 00:10:50.000 SEA - Sane: there's a set of agents that are driving the most sessions, and those are obvious areas of focus. And there's a set of agents…


00:10:49.000 --> 00:10:51.000 Wenlong Dong: Hmm.


00:10:50.000 --> 00:10:54.000 SEA - Sane: But a lot of friction, and those are also obvious areas of focus.


00:10:54.000 --> 00:11:01.000 SEA - Sane: agents that have low friction, low sessions, we should just ignore, I think, for a while. We'll have to watch that, that might change, but, like.


00:10:59.000 --> 00:11:01.000 Wenlong Dong: Mhm.


00:11:01.000 --> 00:11:10.000 SEA - Sane: I mean, just my initial thing here, like, Monist doesn't have intern access, and my claw is, like, a silly experiment, so, like, probably we're not focusing on those yet.


00:11:01.000 --> 00:11:03.000 Wenlong Dong: Hmm.


00:11:10.000 --> 00:11:16.000 SEA - Sane: But Analytics Agent has huge friction, and Cloud Code has huge usage. Those are places to start. So that's where my mind is going in terms of.


00:11:16.000 --> 00:11:18.000 SEA - Sane: Prioritization.


00:11:17.000 --> 00:11:23.000 Wenlong Dong: Right. By the way, this scoring is based on the posts, right? There's… it's not based on other…


00:11:21.000 --> 00:11:33.000 SEA - Sane: Yeah, yeah, yeah. We can… yeah, yeah. Yeah, but see, that's what I'm saying. When I'm thinking about the data here for this grid, like, it would be… we'd some balance of frequency and frequency of usage and frequency of friction.


00:11:33.000 --> 00:11:43.000 SEA - Sane: Um, to prioritize it, and… and… and because I think, like, you know, to your point, posts are great, but sometimes you get some very, you know, a lot of posts about my claw when really that isn't the thing that matters.


00:11:33.000 --> 00:11:35.000 Wenlong Dong: Right.


00:11:43.000 --> 00:11:45.000 SEA - Sane: So, yeah.


00:11:45.000 --> 00:11:46.000 Wenlong Dong: That's right, yeah.


00:11:46.000 --> 00:11:55.000 Can Lin: Tony, I agree with you, right? But I think just one caveat, I think when it was called out in the document, right? For example, even for my callout, right, is, uh.


00:11:55.000 --> 00:12:15.000 Can Lin: Uh, it has… right now has no friction, because it runs dangerously a lot of permissions, right? So it's… but I think, uh, from this program perspective, you know, I was thinking maybe we can still treat this more on the risk side. The risk needs to be minimized, right, and then we target friction, or are you thinking about we target both at the same time? Basically, this table, right, we only look at the friction.


00:12:15.000 --> 00:12:19.000 Can Lin: as of now, there are areas that are taking more risk.


00:12:16.000 --> 00:12:18.000 Wenlong Dong: Yeah.


00:12:16.000 --> 00:12:18.000 SEA - Sane: Yeah.


00:12:19.000 --> 00:12:21.000 Wenlong Dong: Right, right.


00:12:20.000 --> 00:12:26.000 SEA - Sane: I think there's an agent… there's an agent oversight program that you're also in, CAN, that I think has this version of… with risk on it.


00:12:24.000 --> 00:12:26.000 Can Lin: Yep.


00:12:26.000 --> 00:12:34.000 Can Lin: Once they solve their problem, and then this role will be higher up, and then we'll focus, right? I think that's a good handle.


00:12:26.000 --> 00:12:28.000 SEA - Sane: I think.


00:12:30.000 --> 00:12:31.000 Wenlong Dong: Yes.


00:12:33.000 --> 00:12:34.000 SEA - Sane: Yeah.


00:12:35.000 --> 00:12:37.000 Wenlong Dong: Hi, Rachel.


00:12:36.000 --> 00:12:47.000 rachellee: Yeah, kind of related, do we… is there any point or value to us distinguishing between good or expected friction, or… and bad or unexpected friction?


00:12:48.000 --> 00:12:54.000 rachellee: Because I don't think our goal should be to drive friction down to zero, right? Like, there's some friction still.


00:12:52.000 --> 00:12:54.000 SEA - Sane: Yeah, yeah.


00:12:55.000 --> 00:13:06.000 SEA - Sane: Let me answer how we did this last half with spare. So, yes, we can't get to zero. Um, if the outcome-based is basically what you're describing, I don't think we can today measure outcome-based.


00:13:06.000 --> 00:13:15.000 SEA - Sane: So I think what we should do is, first off, you know, look at the overall number as our goals, and then target things that we… like, interventions that we think want to drive down bad friction.


00:13:15.000 --> 00:13:22.000 SEA - Sane: Over time, we'll have to kind of figure out where, you know, where is the line of good versus bad. The way we did it last time was we used UXR to.


00:13:23.000 --> 00:13:30.000 SEA - Sane: Basically talked to users a lot, and started getting a sense of, like, when they effectively stop complaining, and then we called that good.


00:13:31.000 --> 00:13:33.000 rachellee: Alright.


00:13:32.000 --> 00:13:39.000 Wenlong Dong: Yeah. Yeah, uh, do you know the, uh, the percentage of the.


00:13:39.000 --> 00:13:45.000 Wenlong Dong: of the good friction among the overall, I mean, the reason why I ask is that.


00:13:45.000 --> 00:13:53.000 Wenlong Dong: Uh, how… I want to know how serious this problem is, so that we can sequence this problem to solve, right?


00:13:54.000 --> 00:13:56.000 Wenlong Dong: So, tell me, uh…


00:13:55.000 --> 00:14:02.000 SEA - Sane: Yeah, I'm just trying to… I'm trying to make… think about how to answer your question. To use an example, so for last half with Data Warehouse.


00:14:02.000 --> 00:14:04.000 SEA - Sane: When we started getting down to, like.


00:14:04.000 --> 00:14:10.000 SEA - Sane: single-digit interruptions per half. People weren't complaining anymore. That's a pretty low…


00:14:10.000 --> 00:14:19.000 SEA - Sane: like, a low number, but warehouse interruptions were really severe. Like, you'd have to wait days, and it was opaque and all that. So, there's, like, two… there's two things here. One is, like.


00:14:19.000 --> 00:14:30.000 SEA - Sane: you know, is the interruption fast? Can I get unlocked quickly? Though people are more tolerant of those, and they're less tolerant of long interruptions.


00:14:30.000 --> 00:14:42.000 SEA - Sane: I don't think long interruptions are a thing here, though. It's more like, is my agent actually doing the thing it's supposed to do? So, to finish my thought here, I think we actually have to eventually get into some level of outcome-based friction.


00:14:42.000 --> 00:14:53.000 SEA - Sane: or at least outcome-based on the sessions to start saying, you know, are we actually getting, you know, what percentage of these are resulting in something that is not what we want? And that's where we'll find our threshold.


00:14:55.000 --> 00:14:57.000 Wenlong Dong: Hmm.


00:14:57.000 --> 00:15:02.000 SEA - Sane: Sorry, I don't have a hard number answer here. It's a little bit different from…


00:15:00.000 --> 00:15:02.000 Wenlong Dong: Okay.


00:15:02.000 --> 00:15:04.000 Wenlong Dong: I got it, thank you.


00:15:06.000 --> 00:15:08.000 Wenlong Dong: Uh, hold on.


00:15:06.000 --> 00:15:12.000 Tola Dalton: Yeah, just kind of thinking through this, also, my point was going to be related that I think.


00:15:12.000 --> 00:15:17.000 Tola Dalton: Lens 1 makes sense, because it… the friction matters even if the agent.


00:15:18.000 --> 00:15:21.000 Tola Dalton: Uh, it ultimately finds its way around.


00:15:21.000 --> 00:15:30.000 Tola Dalton: But ideally, we'd have a way of prioritizing ones that are more outcome impacting above.


00:15:30.000 --> 00:15:36.000 Tola Dalton: other friction, and right now, I feel like we're kind of perhaps treating all equal.


00:15:36.000 --> 00:15:40.000 Tola Dalton: But, um, Tony, I think if I'm understanding correct.


00:15:40.000 --> 00:15:50.000 Tola Dalton: the outcome-based, that's a really difficult thing. We don't really know how to quantify the hard blocks, where, okay, we saw some friction, you know, in the axis.


00:15:50.000 --> 00:16:00.000 Tola Dalton: Uh, example, we had an actual deny, we saw it resulted in something, um, some kind of error, some kind of, uh, consequence in the agent trace.


00:16:01.000 --> 00:16:07.000 Tola Dalton: But then the next level is, like, did the agent ultimately find a way around, or… or stop?


00:16:06.000 --> 00:16:13.000 SEA - Sane: Right. I think we can find the hard blocks, right? You know, we know when it stops, and like, for example, we know.


00:16:13.000 --> 00:16:15.000 Tola Dalton: Okay.


00:16:13.000 --> 00:16:18.000 SEA - Sane: if it creates a task when it stops. Like, that's a pretty good sign of, like, something has gone disastrously wrong.


00:16:18.000 --> 00:16:27.000 SEA - Sane: Um, so, like, those are, like, fairly easy in my mind to prioritize. What I find difficult is the agent hits a block, it decides to do something different.


00:16:28.000 --> 00:16:29.000 SEA - Sane: Was that good or bad?


00:16:29.000 --> 00:16:31.000 Tola Dalton: Yeah.


00:16:30.000 --> 00:16:31.000 SEA - Sane: I don't know.


00:16:33.000 --> 00:16:44.000 Tola Dalton: Yeah, and I think maybe that's… that's where just the quantification of those blocks is kind of all we've got, like, the volume of these blocks, and then they're still, um, valid to, uh.


00:16:40.000 --> 00:16:42.000 SEA - Sane: Yes.


00:16:44.000 --> 00:16:46.000 Tola Dalton: valid to…


00:16:46.000 --> 00:16:57.000 Tola Dalton: address, but I do think it would be great to get a real kind of criteria in terms of the ones that end up as those hard blocks that we bubble those up, and even if they're.


00:16:57.000 --> 00:16:59.000 SEA - Sane: Yep.


00:16:57.000 --> 00:17:05.000 Tola Dalton: Uh, relatively lower in number than, you know, something that might happen a lot, but the agents always find a way around, then we can… we can prioritize this higher.


00:17:05.000 --> 00:17:07.000 SEA - Sane: Yeah.


00:17:06.000 --> 00:17:14.000 Wenlong Dong: Alright, I think Ken has given a lot of thoughts, maybe let's see, Ken, uh, so, uh, Anisha, do you want to go first, or…


00:17:15.000 --> 00:17:20.000 Anisha Patel: So, kind of, if you had to continue to… yeah, yeah, go ahead.


00:17:18.000 --> 00:17:23.000 Can Lin: Yeah, isn't it? I want to create common, again, creating common down this, right? Um…


00:17:23.000 --> 00:17:32.000 Can Lin: I do think that the outcome-based is probably something you eventually want to go, right? But I also agree with Tony, and we know is that probably the, um.


00:17:32.000 --> 00:17:44.000 Can Lin: interruption-based is a good starting point for us, because even for taking the warehouse friction and the spare as example, right, I think what's important for us right now is that the metrics is.


00:17:44.000 --> 00:17:51.000 Can Lin: at least directionally aligned with our prioritization, right? As long as that condition is met, and then…


00:17:51.000 --> 00:18:05.000 Can Lin: basically, it unblocks us, and then we keep refining the metric, because I think the outcome based only matters more when we say, hey, we already cut all the fat, and the obvious section should not be there, and then we are at the last.


00:18:05.000 --> 00:18:13.000 Can Lin: like, a few miles, and then we need to, like, drill down to really understand it, right? But right now, there are just so many frictions all around there, I think, uh.


00:18:14.000 --> 00:18:19.000 Can Lin: as long as we pick those big buckets, I think it's very unlikely we get it wrong, and uh…


00:18:19.000 --> 00:18:22.000 Can Lin: So I think that's… that could be a balance for us.


00:18:24.000 --> 00:18:26.000 Wenlong Dong: Okay.


00:18:25.000 --> 00:18:37.000 rachellee: Yeah, that makes sense. Um, I was thinking also, like, some of the prior art we did with spare might not apply here super well, because maybe if we are measuring interruption for agents.


00:18:37.000 --> 00:18:54.000 rachellee: users don't necessarily see that, or they don't care, right? Because agents, like, try all these different paths, and at the end of the day, like, get the job done, or whatever. So maybe, like, if we do a UXR kind of thing, and say, like, hey, like, did you like this or not? Maybe users might not even know, um, how many interruptions that agents run into.


00:18:54.000 --> 00:19:03.000 rachellee: Or even, like, if access was the reason, like, this task failed, or whatever. It's more like a black box to users, right?


00:19:04.000 --> 00:19:08.000 SEA - Sane: I mean, I want to sit in there. I… you're right, but, like, here's my worry.


00:19:10.000 --> 00:19:12.000 SEA - Sane: We have known… okay.


00:19:13.000 --> 00:19:21.000 SEA - Sane: I'm pretty sure that if you tell an agent to go, like, say, run a query against this table, and it goes and runs against a different table, that's not going to be what I want.


00:19:21.000 --> 00:19:30.000 SEA - Sane: Like, I'm pretty sure about that. There's going to be instances, to your point, where the agent makes, like, a great, like, effectively says, oh, that wasn't what I should do, and I'll make some other decision.


00:19:30.000 --> 00:19:35.000 SEA - Sane: But, like, my big worry here is that every time we're deflecting these things, there's adding a chance for error.


00:19:36.000 --> 00:19:39.000 rachellee: Sorry, what are we to… what are…


00:19:38.000 --> 00:19:44.000 SEA - Sane: Every time a security or privacy control deflects an agent to something else, the con… the…


00:19:42.000 --> 00:19:44.000 rachellee: Mm-hmm.


00:19:44.000 --> 00:19:51.000 SEA - Sane: the rate of error, or possible error, goes up. I think it's much more likely that error goes up than error goes down.


00:19:48.000 --> 00:20:05.000 rachellee: Right, yeah, I'm not… yeah, I'm not dis… yeah, I'm not disagreeing with that, right? So, I think what I'm saying is this is true, and it might not always, uh, be visible to the user. Like, I think there are cases where it'll be, right? Where agents did something completely wild, and there's, like, a…


00:19:51.000 --> 00:19:53.000 SEA - Sane: Yeah.


00:20:02.000 --> 00:20:04.000 SEA - Sane: Yes.


00:20:05.000 --> 00:20:21.000 rachellee: like, failure. Um, but I think there may be also cases where agents did… this is kind of similar to when you're talking about, like, requesting ACL permission for an employee that's a high friction event because you have to wait for days, or whatever, but if your agent is trying all these things, and then at the end says, like, oh, I'll try this thing.


00:20:22.000 --> 00:20:30.000 rachellee: maybe that is not as significant. So I'm saying it will not always translate to user complaining about it, if that makes sense. And these are not…


00:20:28.000 --> 00:20:33.000 SEA - Sane: I agree, but let's say it translates to the wrong answer. The user might not complain.


00:20:31.000 --> 00:20:42.000 rachellee: Yeah, yeah, yeah, I'm saying, yeah, so absolutely, absolutely, right? And these are not mutually exclusive things. All I'm saying is it'll turn into wrong answers sometimes, but not all the time.


00:20:32.000 --> 00:20:34.000 Wenlong Dong: Yeah.


00:20:38.000 --> 00:20:40.000 SEA - Sane: Yeah.


00:20:42.000 --> 00:20:51.000 SEA - Sane: I agree, and then my point is, each interruption adds to the chance of turning into the wrong answer or the wrong thing, which is why I think interruptions is the right place to start, because.


00:20:42.000 --> 00:20:44.000 Wenlong Dong: Right.


00:20:51.000 --> 00:20:54.000 SEA - Sane: It's like compounding error to me.


00:20:54.000 --> 00:20:59.000 Wenlong Dong: Right, uh, there are two other metrics, uh, I chatted with the client yesterday. One is, uh.


00:20:59.000 --> 00:21:10.000 Wenlong Dong: latency, right? How long does it take for the agent to finish the work? If you… if there are interruptions, it could delay that. That's one thing. The other is about the cost.


00:21:11.000 --> 00:21:22.000 Wenlong Dong: how many tokens are used to finish the work, right? So these are other things. Yeah, users may not expect that too much, but behind the scenes, there's a lot of impact.


00:21:22.000 --> 00:21:27.000 rachellee: Right. So should… do you think we should be tracking that as well?


00:21:22.000 --> 00:21:24.000 Wenlong Dong: Yeah, that's right, yeah.


00:21:28.000 --> 00:21:34.000 Wenlong Dong: Right now, uh, there… there's one metric here, so… so that's… maybe… maybe we can brainstorm more on that.


00:21:35.000 --> 00:21:40.000 Wenlong Dong: So, I think this room sounds like we're converging to this primary.


00:21:40.000 --> 00:21:46.000 Wenlong Dong: or the next one, right? But we still worry that the next one is maybe skewed.


00:21:46.000 --> 00:21:57.000 Wenlong Dong: So, one thing I'm thinking is that maybe we can measure those cases, if possible, or… or, like, the outcome-based measurement, if possible, or we can…


00:21:58.000 --> 00:22:03.000 Wenlong Dong: Uh, like, do the eval, right, and build the eval framework to…


00:22:03.000 --> 00:22:09.000 Wenlong Dong: And then identify which frictions or which interruptions are.


00:22:09.000 --> 00:22:16.000 Wenlong Dong: okay, and which are not okay. I think the okay interruptions are the ones which.


00:22:16.000 --> 00:22:27.000 Wenlong Dong: Uh, which we definitely don't want the agents to circumvent, right? They needed to hear that. If that's the case, then all of the other interruptions, I think, are just, uh.


00:22:27.000 --> 00:22:29.000 Wenlong Dong: Joseph Fergent. Real Fergent.


00:22:32.000 --> 00:22:48.000 Can Lin: And maybe I want to quickly comment on what Rachel said here, and if I understand correctly. I do think there is a one dimension maybe worth calling out as a secondary of the lens 1, right, is basically the difference between interactive versus not.


00:22:32.000 --> 00:22:34.000 Wenlong Dong: Okay.


00:22:48.000 --> 00:23:04.000 Can Lin: Because I do think there's a difference, like, hey, a person sitting in front of the agent, and then we interrupted, versus, hey, go ahead and join it, and then the agent runs, right? And I think they also drop the next one, but I think the first people are more sensitive, for example, personally.


00:23:04.000 --> 00:23:16.000 Can Lin: Like, even, like, some command running slower because of, like, some cooks there, and it's very destructive to me, right? But if I have my agents autonomously run, that doesn't matter.


00:23:16.000 --> 00:23:29.000 Can Lin: So that can be one drill down end of the lens, and that… because even, Tony, right, even in the data space, we actually focus on the ad hoc queries the most, right? That's basically people directly experiencing it.


00:23:30.000 --> 00:23:37.000 SEA - Sane: Yeah. I think that's reasonable. Here's what I propose. First off, because we, in fact, need actionable data.


00:23:37.000 --> 00:23:44.000 SEA - Sane: I can't build the outcome-based thing today. So, I think interruption is a reasonable thing to build on right now.


00:23:44.000 --> 00:23:49.000 SEA - Sane: Um, I think adding that dimension makes sense, Ken, because it'll give us some intuition, but we should also send UXR after that.


00:23:49.000 --> 00:23:53.000 SEA - Sane: And, like, start figuring out… yes, obviously people will feel pain from…


00:23:53.000 --> 00:24:03.000 SEA - Sane: interactive interruptions, but are they also feeling pain from non-interactive ones? Like, I used… I got an answer, and I used it in a meeting, and someone said that's wrong as pain, even if it comes, you know, two days later.


00:24:03.000 --> 00:24:10.000 SEA - Sane: Um, so we should investigate that. And then I think after we get all this squared away, and we, like, are happy with it, we should start working on outcome-based.


00:24:11.000 --> 00:24:16.000 Wenlong Dong: Okay. So, let's see, we have 2 minutes. I'm wondering whether we can wrap up on that next.


00:24:16.000 --> 00:24:21.000 Wenlong Dong: up here, I think at least that we have a very good discussion here, and uh…


00:24:21.000 --> 00:24:29.000 Wenlong Dong: And, uh, we can also do the offline, like, uh, like, comments, or in the dark, or discussions about.


00:24:29.000 --> 00:24:38.000 Wenlong Dong: One is that do we agree with these dimensions and also the focus of the… of the measurement, and then…


00:24:38.000 --> 00:24:43.000 Wenlong Dong: Uh, maybe we can also start to think which ones are the top.


00:24:43.000 --> 00:24:54.000 Wenlong Dong: Uh, pipeline metric. And after that, I think we need to kick off the observability very quickly, which is here, sorry.


00:24:54.000 --> 00:24:57.000 Wenlong Dong: the observability…


00:24:57.000 --> 00:25:07.000 Wenlong Dong: logic is that what are all the choke points that we need to do the logging, right? And, uh, how can we collect a certain full logging, uh, together?


00:25:08.000 --> 00:25:10.000 Wenlong Dong: Um…


00:25:10.000 --> 00:25:15.000 Wenlong Dong: So I chatted with Rachel briefly offline. Uh, we can have a…


00:25:15.000 --> 00:25:23.000 Wenlong Dong: two engineers, one from the Agent Observatory Wall Street, and one engineer from the packaging to partner together to.


00:25:23.000 --> 00:25:28.000 Wenlong Dong: To… to… and also check with you guys to see whether login is already available.


00:25:28.000 --> 00:25:34.000 Wenlong Dong: And WLogin is not available yet in order to fill out this table, right?


00:25:34.000 --> 00:25:40.000 Wenlong Dong: So that, uh, so I think that's an urgent follow-up that we need to generate all this, like, a session for.


00:25:40.000 --> 00:25:45.000 Wenlong Dong: login, so that a measurement can be… can be done next. Does that make sense?


00:25:45.000 --> 00:25:49.000 SEA - Sane: Wenlong, who's taking that long? I agree with that. Who's taking that item?


00:25:50.000 --> 00:25:55.000 Wenlong Dong: This one, uh, right now, the login, login side, uh…


00:25:51.000 --> 00:25:53.000 SEA - Sane: The logging item.


00:25:55.000 --> 00:26:03.000 Wenlong Dong: So Rachel already identified one engineer, and the other one, I'm waiting for Absorbusyside to provide later today.


00:25:58.000 --> 00:26:00.000 SEA - Sane: Okay.


00:26:03.000 --> 00:26:05.000 Wenlong Dong: And then they will start to do the logging.


00:26:03.000 --> 00:26:05.000 SEA - Sane: So…


00:26:05.000 --> 00:26:07.000 SEA - Sane: So, just tactically.


00:26:05.000 --> 00:26:09.000 Wenlong Dong: Uh, I mean, not do, like, check your existing login.


00:26:09.000 --> 00:26:17.000 SEA - Sane: tactically, we can start building out this categorization based on what we have. If we can get the logging in there quickly, we should use the current source.


00:26:17.000 --> 00:26:27.000 SEA - Sane: If we can't, I can go after other existing things and start unioning them together, basically. I'd kind of rather not, if we can get the logging in here quickly, but I don't know what the answer is there, so…


00:26:18.000 --> 00:26:20.000 Wenlong Dong: Right.


00:26:27.000 --> 00:26:30.000 Wenlong Dong: Uh, Connor?


00:26:30.000 --> 00:26:40.000 Tola Dalton: I'd love to stay close on this one because, um, to make sure that we're plugging into existing efforts as well. So, for example, we've got a daily working session going for access friction.


00:26:40.000 --> 00:26:51.000 Tola Dalton: and logging, um, Deepra from the DS side, and I've got an engineer in my team, um, who's working on filling logging gaps that we find in Aqual Checker-related logging.


00:26:51.000 --> 00:26:56.000 Wenlong Dong: Okay. Who… who… can you… can you provide the appeals? Yeah, maybe we have…


00:26:52.000 --> 00:26:54.000 Tola Dalton: So, it would be good to take level.


00:26:56.000 --> 00:26:59.000 Wenlong Dong: Uh, the POCs can work together on that.


00:26:59.000 --> 00:27:01.000 Tola Dalton: That would be great.


00:27:01.000 --> 00:27:05.000 Wenlong Dong: Okay. Can you, can you put the name, uh, here, and then we can…


00:27:02.000 --> 00:27:04.000 Anisha Patel: Hmm.


00:27:05.000 --> 00:27:07.000 Wenlong Dong: Okay, well, what is it?


00:27:05.000 --> 00:27:08.000 Tola Dalton: Yeah, where's this doc link, by the way?


00:27:08.000 --> 00:27:11.000 Anisha Patel: It's in the agenda notes, Tola.


00:27:08.000 --> 00:27:11.000 Wenlong Dong: Uh, in the invite, the first…


00:27:10.000 --> 00:27:13.000 Tola Dalton: And the invite? Okay. I can… I can take…


00:27:11.000 --> 00:27:18.000 Wenlong Dong: Oh, actually, we have two, uh, items, agenda items today, right? But we only finished one.


00:27:18.000 --> 00:27:25.000 Anisha Patel: Yeah. I am… so I think we are about time. Questioned… this was really helpful, thank you, Wenlong.


00:27:25.000 --> 00:27:33.000 Anisha Patel: And team, uh, should we do daily stand-ups for now, on this effort, until we feel comfortable with the…


00:27:34.000 --> 00:27:36.000 Anisha Patel: Production.


00:27:38.000 --> 00:27:41.000 rachellee: Maybe let's do twice weekly.


00:27:41.000 --> 00:27:43.000 Anisha Patel: Twice a week.


00:27:44.000 --> 00:27:47.000 SEA - Sane: Something to keep the momentum up is good.


00:27:44.000 --> 00:27:46.000 Wenlong Dong: That's…


00:27:46.000 --> 00:28:01.000 Anisha Patel: Yeah, how, uh, is it okay if we do at least, um, I think at least 3 times next week, Rachel and team, um, and if we feel, we can taper down the frequency after that, but I think once we have the measurement in place, it will be good for overall work stream.


00:27:57.000 --> 00:27:59.000 Wenlong Dong: No.


00:28:01.000 --> 00:28:03.000 Anisha Patel: Overall program direction.


00:28:03.000 --> 00:28:12.000 rachellee: Yeah, actually, I'm gonna be out, uh, starting Thursday, so you… y'all can meet as many times as you want.


00:28:09.000 --> 00:28:11.000 Wenlong Dong: Mm-hmm.


00:28:11.000 --> 00:28:13.000 Wenlong Dong: Oh.


00:28:13.000 --> 00:28:19.000 Wenlong Dong: Okay. Uh, yeah, maybe… if you are okay, maybe 3 times.


00:28:19.000 --> 00:28:24.000 Wenlong Dong: A week next week, and I hope that we can finish this in 2 weeks, if possible.


00:28:25.000 --> 00:28:30.000 Wenlong Dong: And then we can, like, start to share that strategy.


00:28:31.000 --> 00:28:33.000 Wenlong Dong: Does that make sense?


00:28:33.000 --> 00:28:37.000 Wenlong Dong: Okay. Uh, by the way, if you feel that who else should it be?


00:28:38.000 --> 00:28:44.000 Wenlong Dong: Involved here, we can also, uh, add, based on these patterns.


00:28:44.000 --> 00:28:48.000 Wenlong Dong: If we don't feel that we have full coverage of this.


00:28:48.000 --> 00:28:50.000 Wenlong Dong: We may add.


00:28:51.000 --> 00:28:53.000 Wenlong Dong: One or two people, if needed.


00:28:55.000 --> 00:28:57.000 Wenlong Dong: Okay. Okay, thank you, guys.


00:28:57.000 --> 00:29:00.000 Anisha Patel: Thank you. See you on the other call. Bye!


00:28:59.000 --> 00:29:01.000 Wenlong Dong: Perfect. Bye.


