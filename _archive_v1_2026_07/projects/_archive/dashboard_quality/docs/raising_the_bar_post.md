<!-- Source: https://fb.workplace.com/groups/197295836397052/permalink/458302390296394/ -->
<!-- Title: Raising the Bar Post — Raising the Bar for Privacy Dashboards -->
<!-- Author: Tony Harper -->
<!-- Date posted: 2024-12-05 -->
<!-- Date accessed: 2026-03-31 -->

# Raising the Bar for Privacy Dashboards

We've talked a **LOT** over the last few years about dashboards. Justin Gourley got us started with certification and dashboard reviews back in 2022. We built up DEVizED and the DE/DI Data Visualization SME group. We brought Privacy DE into the fold and certified our backlog.

We've done a lot but we have a lot further to go. In my opinion, every single dashboard we build should have the following qualities:

- Has clear purpose, narrative, and relevance to its audience
- Easy to understand
- Fast
- Accurate
- Bug-free

Dashboards are the most visible part of a Data Engineer's output. As a Data Engineering org, we must build the systems, processes, and craft to get these right. My vision for the Privacy DE org is that we hone our craft, and by the end of 2025 are consistently building and maintaining high quality dashboards that not only meet the minimum standards but that are well regarded as highly accurate and easily usable sources of information across the PCP and PPG orgs.

As such, we all need to make sure that we do a few things very well:

- Make dashboard certification part of your dashboard release process
- Move to canonical representation of the metrics on your dashboards
- Design your dashboards with a narrative flow and pressure test your users to ensure that they make sense

## Dashboard Certification is the Bare Minimum

I receive this question frequently: "Why do I have to certify my dashboard? My dashboard is pretty good, isn't that clear from looking at it?"

Dashboard Certification is our method by which we raise the floor for dashboards. It is our common method for ensuring that dashboards are fast enough, follow standard design principles, and that someone is actually looking at them before they are released. This is your dashboard diff review. This is how you make sure you didn't miss something crucial. You must do this.

If your dashboard already meets these criteria, certification is quick and easy. If it does not, certification will catch them and guide it to a better place. **This is not optional, and each of us must build in time to build dashboards against our standards and time for dashboard certification in our projects.**

I also expect everyone to keep their dashboards in compliance over time. As you receive tasks to fix issues with ongoing certification, please find time to work them by their due date.

## Canonical Metric Representation is Critical

Dashboard Certification improves the user experience of a dashboard, but does not guarantee data quality or accuracy. One pernicious and subtle issue with dashboard data is using the wrong version of a metric, either via using a deprecated table, having an error in a query, or just pulling the wrong data.

Metric 360 aims to house the Canonical representations of every metric that we own, and as such we should strive to build it out, govern it, and -- critically -- use it on our dashboards.

To that end, I would like to see every new metric intended to be used in a dashboard or experimentation to be created through code M360, and every dashboard use these M360 metrics wherever it is technically possible. I also expect all technical blockers to be flagged to our M360 working group so that they can be resolved. Finally, I expect metrics that we are moving on from to be formally deprecated and archived from M360 when the time comes.

This will require upfront work that will pay off later when metrics can be reused and are unmistakably the right ones to put on our dashboards. **Please budget for this time in your roadmaps going forward, starting in H1 2025.**

## Designing for Narrative and Usability is Raising the Bar

All that said, it is entirely possible to build a dashboard that is performant, accurate, and compliant, and still have it not work for its users. Dashboards, like any data presentation, need to make sense to their users for them to be impactful and used in decisionmaking.

Unlike dashboard certification or M360, there is no **formula** for making sure your dashboard is well designed and has a solid narrative that makes sense to its users. There is no easy button here. This is where we, as the Privacy DE team, need to **raise the bar** in terms of how we approach dashboard design, usability testing, and the post-launch feedback loop.

There's not a great playbook here yet, but here's how I've personally approached this over the years:

1. **Start by identifying your most important users by name.** This cannot be overlooked. If you are building a dashboard and do not know who specifically will use it, you will almost certainly build the wrong thing. Go find out who will be using this, and go beyond your immediate XFN. In Privacy we frequently build for the company. If these users have different needs, create a user segmentation and ask yourself if this segmentation requires one dashboard, multiple tabs, multiple dashboards, etc.

2. Working with your users, **create a clear list of questions** that the dashboard is intended to answer, mapped to representative users and situations where they will be asking them. Map out the dimensions that you want each answer to be sliceable by. If your users are already answering these questions manually, sit with them and have them show you how they do it. **Do everything you can to understand the user and their mindset.**

3. **Check the questions and dimensions for cohesiveness.** If the questions seem to be unrelated to one another, if they'll be used in very different settings, if different users have wholly different questions from other users, you should consider splitting the dashboard into multiple tabs to group like questions. Similarly, if the dimensions do not apply to all metrics, consider splitting.

4. **Design the dashboard on paper before you build it.** For me, that literally means sketching it out in my notebook, but that can be any tool that you find useful, such as Excalidraw or Lucid. Before building, walk through each of the users and situations your users will be facing. Ask yourself -- how easy is it to answer those questions for this user? Are the widgets presented in a linear fashion according to how they'll be asking questions? Will answering them require a lot of back and forth and thus take a lot of time? Adjust your design accordingly.

5. **Quickly build a v0 of the dashboard** to test initial functionality, filters, and metrics, even if you have to use placeholders. This will allow you to get early feedback and test out the functionality and narrative yourself.

6. After you build your dashboard, **use it yourself for a period**. If there is reporting to be done, do that reporting yourself from the dashboard. If it is to be used in reviews, go to those reviews and answer the questions yourself instead of deferring to your XFN or your manager. **There is no substitute for using your own dashboard in order to get design feedback.**

7. After dashboard launch, check in periodically with your users and get feedback. So long as the dashboard is a living thing, have a feedback loop in place and actively make sure that you understand how well your dashboard is meeting your users' often changing needs. **When it comes time, archive the dashboard in favor of something else.**

## Great Dashboards - and beyond - are Part of Data Engineering's Future

It is my strong contention that great dashboards are a part of DE's present and future. As our dashboarding technology improves with great tools like Vega Lite and Explore Mode, the stage is set for Data Engineering to make even more product impact through amazing dashboards.

And as we look to a future with GenAI and other emerging technologies, perhaps we can imagine even more sorts of automation, with Metrics Bots providing updates in forums where our users gather and LLMs providing email and presentation summaries of the data. I want to see Privacy DE leaning into all of this and contributing to the future of data visualization and beyond at Meta.
