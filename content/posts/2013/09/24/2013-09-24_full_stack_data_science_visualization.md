Title: Full Stack Data Science: Visualization Tools Edition
Author: Ross Donaldson
Date: 2013-09-24 07:43
Slug: 2013-09-24_full_stack_data_science_visualization
Category:
Tags:
Summary:
status: draft

I work in idiosyncratic ways. Truthfully, it's not something I've done on purpose. In my career so far, the weird way has often also been the way I could get what I want to get done the fastest. _Exemplus gratis_: when I realized a need to access data in a data warehouse hosted by my company's parent company, I had roughly these choices:

1. Be told, very firmly, I was doing it wrong.
2. Be told what I needed to do was pretty much impossible without a Windows machine[^win].
3. Teach my R server how to spin up a tiny JVM, load in the JDBC drivers for the data warehouse in question, and use R as my Netezza frontend, by way of emacs.

So obviously I went with number three; I always go with number three. Any time I'm told "that can't be done" or "we'll need to get the budget for more resources" or "you can't get there from here!", I have this one-two punch of pathological disbelief and obstinate, defiant "Oh yeah, watch me!" The upside is my reputation for Getting Tricky Crap Done. The downside is... well.

The downside is the vast and not always easy to perceive set of problems that come with being the only person who knows the tools they use. I have no code reviews. Nobody can check my work. I doubt anybody else could _use_ my work if they had to -- it's highly non-transferable, which raises (for me, anyways) some very uncomfortable questions about efficiency and information gatekeeping. Perhaps the problem I deal with the most regularly is this: how do I share my work?

Lets consider a common use case:

Me: "Hey boss, I have the Visualization you asked for."
Boss: "Terrific. Can you send me the Excel sheet? I want to pivot this."

Did you know you can get an Android widget that just plays the Sad Trombone? I have it. I keep it around for times like this. **wop-wah** Because there is no Excel sheet -- of course there isn't. For two reasons: 1. Typically I load data in to R; once there, `ggplot2` makes a billion times more sense than Excel; 2. I can barely use Excel. Like barely. At all. Seriously.

This post actually started from my desire to write a grudging and eventual indictment of Excel -- but the farther I got with that line of thinking, the more I realized I was writing about a separate-but-related problem -- or maybe two problems, really. The first I'll call Data Stories. The second I'm calling either Cognitive Load or Conceptual Schism. We'll see which one sticks.

### Data Stories

Information is data made relevant. The only analysis I ever want to do is analysis that informs a decision or enables action; for that to be true, an analysis has to result in the production of information. A visualization tells a story about information that conveys data -- and the data is still there in the background. I particularly value working in places with a culture of data -- a place where people are accustomed to asking questions about what the information _is_, where the data _came from_, and can they see it for themselves? This leads me to believe, pretty firmly, that if you are producing a report on a topic, the data is as much a part of that report as the polished visualizations are.[^dataexcep] Not everybody will want to get up to their elbows in the data, but everybody should have the choice.

This conviction leads, frankly, to some pretty awkward money-where-my-mouth-is moments, particularly when it comes time to build a report.

[^win]: And let me be frank about this: no thanks.
[^dataexcep]: There are exceptions; regular reporting and dashboards, for instance, should expose their data with the understanding that once it's been vetted and questioned once it probably wont be poked at every single time the dashboard goes out.
