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

This conviction leads, frankly, to some pretty awkward money-where-my-mouth-is moments, particularly when it comes time to build a report. After all, this is the gotcha of Excel (which I loathe): _almost everybody_ can open an Excel document, somehow; they can see the calculations, manipulate the charts. You can add your source SQL in blocks of text, which is an unweildy way to be transparent _but it works_. Perhaps most importantly, your information is delivered with the data that backs it, in a format you don't have to be any kind of hacker/dev/data scientist to open and look at.

Of course, if you're anything like me, you also run head-long in to this problem: the code is data too.[^codeisdata] The logical extension of code being data is code being inextricable from the information you've been generating -- in the same way a skeleton is inextricable from a human, code is the framework that holds up the report, the data makes it vital and living. Caveat: the skeleton metaphor extends a step further. Most of the time, you don't meet a person and fuss over their skeleton. For the vast majority of your audience, code may well be noise, and should be included in a way that doesn't knock people out of your data story.

So how do you include the code?

### Conceptual Schism

This is really the idea that got me started on this tear in the first place. It's the breakdown between domain knowledge and product knowledge -- in this specific case, the difference between doing the work of *building* the story and doing the work of *packaging* it. It goes something like this:

> Data work has a core set of skills that are conceptually alike. Computer science, coding, statistics, data visualization: these are all rigorous skills that I find highly inter-operable and a little synergistic (becoming a better computer scientist improves more than just my grasp of computer science). These tasks work the same parts of my brain. When it comes time to package up a report, I suddenly pull out Excel or Tableau -- tools that assume you have some base data you want to load and show. They have as little in common with each other as they do with the work of generating that base data, and being good at Excel or Tableau has _no relationship_, conceptually or otherwise, with being good at data or data visualization or computers at all.

This problem permeates down into some pretty core data tools. SAS and SPSS each have their own ways they want you to work, which are different from Matlab or Octave. While R has a proud, mostly-internally-consistent heart, every R package operates on a completely different set of design metaphors that every other package.[^rpkg] The upside is that it's all programming; the downside is having to learn something thorny and new to speed up already difficult tasks. Tools like Excel or Tableau are even worse, operating on design metaphors that don't make an elegant conceptual transition from slogging about in code.

Lets consider:

#### Excel

This is sort of the default for presenting some kind of data. If you're anything like me, you grew up with Excel in the classroom, typing in your physics homework or making charts about the GDP of Zambia.[^zambia] We all know this is true: Excel was never intended for two thirds of the nonsense it's used for. Excel is for Spreadsheets. Keeping ledgers. Light-weight analysis like marginal sums. Nothing like what it's used for.

I've touched on the upsides all ready: Excel is everywhere. Excel has become the _lingua franca_ of passing around data to anybody who might want to mess with that data themselves. Excel is the go-to for reports at my current company -- we email Excel files out daily, upload them to servers, distribute them far and wide. I'm both stunned and horrified at the ways I've seen people make Excel dance -- from interactive event schedules to self-regenerating pivot tables, so many occult bolt-ons have been added to Excel that very few people can tell you what, specifically, Excel is *for*. It's a hammer; everything is nails.

The thing is: Excel is actually a hammer a la [PHP](http://www.codinghorror.com/blog/2012/06/the-php-singularity.html). In precisely the same way as PHP, it has come to be ubiquitous in the work of data. Consider the problem of the Excel daily dashboard:

You need to send out a daily report for people who want to monitor the pulse of a project. They need to be able to access all your data, fiddle with it, so you build the report in Excel. This works pretty well! Wait, now you need to add something -- well you can just visualize that right in one of the tabs! Perfect. Oh hey, an extra column needs adding, and another -- oh god, did we just change formats on the regular reporting email? Oh hey, you're going on leave? Quick. Teach so-and-so about your reports.

Excel dashboards spiral quickly out of control; they become these living, breathing entities packed with tacit knowledge, and that tacit knowledge is _very difficult_ to discern from looking at a monolithic Excel document. Code can be just as occult and inaccessible, sure, but there are also best practices that we as developers embrace to try and make our code clear, and those patterns are difficult to embrace in Excel, I think.

And lets not even _start_ on all the ways Excel is a fail for those of us who like open source software.

#### Tableau



[^win]: And let me be frank about this: no thanks.
[^dataexcep]: There are exceptions; regular reporting and dashboards, for instance, should expose their data with the understanding that once it's been vetted and questioned once it probably wont be poked at every single time the dashboard goes out.
[^codeisdata]: Yes it is. If anybody tells you different, they are wrong.
[^rpkg]: You can try and do without packages, but that overlooks a huge amount of very good work that will save you important amounts of time -- if you can just figure out how the f%&$! they work.
[^zambia]: Which was totally a place when I wrote a report about it.
