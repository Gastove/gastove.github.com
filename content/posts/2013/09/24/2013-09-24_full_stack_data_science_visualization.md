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

This problem permeates down into some pretty core data tools. SAS and SPSS each have their own ways they want you to work, which are different from Matlab or Octave. While R has a proud, mostly-internally-consistent heart, every R package operates on a completely different set of design metaphors that every other package.[^rpkg] The upside is that it's all programming; the downside is having to learn something thorny and new to speed up already difficult tasks. Tools like Excel or Tableau are even worse, operating on design metaphors that don't make an elegant conceptual transition from slogging about in code. What could be better, after all, than completing your exploratory analysis, getting all geared up to do your full analysis, and... taking a big step back to completely re-invent your process to make it jive with a totally different level of abstraction needed to pull the data into a different visualization framework!

Maybe snakes. Snakes would be better.

### The Use Case

What's the point? What's the core need? What would the _perfect_ thing look like? I think:

1. **Portable**: We need to deliver information to people; that means it needs to be easy to open, with as little specialized software as possible. No skill should be required to _view_ your report.
2. **Self-Serve**: The best thing is when you can put out the birdfeeder and let the birds feed themselves. Generating a report is good; generating a report that self-updates is better. Generating a self-updating report that other people understand how to get what they need from? Fan-damn-tastic.
3. **Parts-complete**: The report should package together source data, process, code, final data set, prose, figures -- the whole works. It should do so without the wrong parts getting in the way at the wrong time.
4. **Transparent**: I mean something slightly subtle here: a report should capture everything it took to make the report. The amount of baked-in tacit knowledge should be very low.
5. **Powerful**: We as data workers have tremendous capacities for imagination, insight, analysis, comprehension; we should be able to fully express ourselves.

### And now, some reporting options

#### Excel

This is sort of the default for presenting some kind of data. If you're anything like me, you grew up with Excel in the classroom, typing in your physics homework or making charts about the GDP of Zambia.[^zambia] We all know this is true: Excel was never intended for two thirds of the nonsense it's used for. Excel is for Spreadsheets. Keeping ledgers. Light-weight analysis like marginal sums. Nothing like what it's used for.

I've touched on the upsides all ready: Excel is everywhere. Excel has become the _lingua franca_ of passing around data to anybody who might want to mess with that data themselves. Excel is the go-to for reports at my current company -- we email Excel files out daily, upload them to servers, distribute them far and wide. I'm both stunned and horrified at the ways I've seen people make Excel dance -- from interactive event schedules to self-regenerating pivot tables, so many occult bolt-ons have been added to Excel that very few people can tell you what, specifically, Excel is *for*. It's a hammer; everything is nails.

The thing is: Excel is actually a hammer a la [PHP](http://www.codinghorror.com/blog/2012/06/the-php-singularity.html). In precisely the same way as PHP, it has come to be ubiquitous in the work of data. Consider the problem of the Excel daily dashboard:

You need to send out a daily report for people who want to monitor the pulse of a project. They need to be able to access all your data, fiddle with it, so you build the report in Excel. This works pretty well! Wait, now you need to add something -- well you can just visualize that right in one of the tabs! Perfect. Oh hey, an extra column needs adding, and another -- oh god, did we just change formats on the regular reporting email? Oh hey, you're going on leave? Quick. Teach so-and-so about your reports. It will take a week; it will not be about analysis or data. It will be about how you make Excel dance.

Excel dashboards spiral quickly out of control; they become these living, breathing entities packed with tacit knowledge, and that tacit knowledge is _very difficult_ to discern from looking at a monolithic Excel document. Code can be just as occult and inaccessible, sure, but there are also best practices that we as developers embrace to try and make our code clear, and those patterns are difficult to embrace in Excel, I think.

And lets not even _start_ on all the ways Excel is a fail for those of us who like open source software.

#### Tableau

This one I have seriously mixed feelings about.

Tableau has the obvious advantage of being purpose built -- and recently -- for the job of doing analysis that shows data. It contains an incredibly powerful engine for getting this job done. Tableau can ingest structured data from almost anything; it can connect to a living data store and update your work as you go, or ingest a SQL statement and load that data locally to dramatically increase analysis speed. Once you're happy with your work, you can publish it to a server, view-able by anybody with the right license.

And the right browser.

On a PC.

Okay, so the wheels kinda just came off, but it's ok, we got this. Have you _seen_ the number of ways Tableau will let you visualize your data? It's completely unreal. You can aggregate, write eloquent equations, add hierarchies and subcategories and groups -- all of which immediately make your data not just explored but explore-able. By other people. You do the work, Tableau bakes in this heady magic that allows other people to wander interactively through your creation. Want to be able to quickly filter your data to show different cohorts? Built-in. Wanna make a dashboard? It's done. Seriously.

And yet.

We just clipped by major beef number one: magic. There's a **lot** of magic. It's everywhere. You poke a button and stuff just _happens_ and it can be completely bewildering and what the hell just happened to my OH GOD WHAT IS THAT? This is an analytics tool with a prominent "back" button. Because you'd never, ever keep your sanity without one. This can be a challenge for somebody accustomed to the _Grammar of Graphics_ approach of `ggplot2`; I expect to take a step and then another step and build up my visualization in layers. Tableau expects me to explore and visualize at the same time, moving through this stack of visualizations I try on like sweaters.

_And it recommends the sweaters_.[^beef] Immensely jarring is the experience of adding another piece to your visualization and watching in dismay as the recommendation engine takes over and everything becomes horribly different. This is a perfectly distinct question from whether or not the recommendations are any good; it's about the wrenching cognitive cost of suddenly trying to decipher something that is entirely other than what you intended or expected.

Have I mentioned that the licenses are hideously expensive? Tableau 8 is changing some of the OS requirements, thank heavens, but this stuff is... an investment, both in money and, frankly, in time. As somebody with a great deal of _intention_ about his work, I'm accustomed to simply writing lines of code that describe what I'd like to see and then adjusting my declarations as needed. Tableau is a different skill. It speaks an entirely different language than the rest of my work. Have I made something excellent in R or Python? Well, that's terrible -- it wont transfer. Sure, I could write my stuff out to a CSV, but Tableau sits on live data! The value of not having to re-run a report is very, very high; I'm not yet sure if it's worth the cost of Tableau.

#### Sweave and IPython Notebooks

Oh darling, darling these things. They are built for me to like them; this is bad news.

[Sweave](http://www.stat.uni-muenchen.de/~leisch/Sweave/) and [IPython Notebooks](http://ipython.org/notebook.html) do roughly the same thing -- that is, they are both ways of writing a document that is code, prose, and code output all together in one place. The implementation details vary; Sweave is for R and builds mostly to LaTeX, while IPN is for (gasp!) Python and is mostly web hosted. The basic gist is uniform: write code, evaluate code, write prose in prose blocks and place code output, compile all together, lead a happy life. I think I'm in love with IPN; I think Sweave might be the best reason I've found to stick with R.

It can't last.

They've got their strengths. The most overt, for me, is that they heal the Conceptual Schism. You aren't just building your report or visualization in the same language as your analysis, you're building the whole thing _at the same time_. It's full stack, consistent from start to end. This makes it beautifully transparent; all the data is captured, as well as the knowledge of how to make the report. Both, actually, are vastly more portable than Excel _or_ Tableau. (LaTeX compiles to PDF; IPN serves a web client that requires no plugins.)

Let's codify the bad news. Let's do it with bullet points:

* These tools? Not sexy. Frequently, not glossy. LaTeX is more or less the gold standard for typesetting mathematics, but beyond that, there's none of the full-color-GUI _snap_ of Tableau or the familiarity (often called "trust") of Excel.
* So far, IPN is deeply good for sharing analytics work with other analysts and not really ideal for sharing reports with people for whom the code isn't first-order information. This can probably be worked around, but it's not the dominant paradigm it was designed for. (If anybody knows of awesome things that prove me wrong on this, oh man, post 'em here.)
* Sweave makes PDFs; that means something that must be downloaded and opened by anybody interested. I feel fine about this, but it's not typically a stand-alone solution. True, Sweave means LaTeX means htmlatex means just use it to typeset an email, hey? Now your email is a zillion pages long and _can't_ be downloaded. Awesome.
** Also, with Sweave... you still have to use R. My thoughts on R really deserve their own post; for now, I'll use a footnote.[^r]
* Any prayer of interactivity is not... here. This is not self-serve. This is not something your boss will take and play with. Sweave at least captures how you _got_ the data; IPN does bake everything in, but there's no "download this data as a CSV" facility unless you make one.

So. That's... a thing.

#### Homebrewed Roll-yer-own Reportfest

This is actually an option and it works. It works about as well as your servers and your databases and whoever you have implementing the code.

Right? Right.

This option is hard. It has some advantages. It works best for regular, daily-dashboard-style reporting, if you're in to that kind of thing. You can, for example, create python scripts that run on a cron job, compile an email, and send it to you for processing Some How Or Another. Depending on your sophistication with python or R, those scripts could generate charts and everything. Maybe the script is actually server code -- a controller plus models, or a service or a module, depending on your particular server idiom. Maybe you have a dedicated analytics DB you can hit? Yeah, I thought not.

This option is both very good and very tricky. It supplements things well; we've had marvelous success with an automated-email-plus-analyst approach. You could automated IPN or Sweave, if you felt like it. Or, you could whole-hog on d3.js and just script up self-serve webpages, if you have some sort of internal portal or admin tool.

This can be the best option and the very, very worst. Given the cost, I'm leery of it; it takes a *lot* of time to set up something like this and to do it well, and once it's done it seldom gets maintained. Besides -- whose perview is it? The server code is the domain of the engineers, but numbers fall under the analysts. Who commits bug fixes, and how are they prioritized? Be wary of this. It can get messy.

### Conclusion

The whole problem with this is that I haven't really concluded anything, myself. There are some powerful tools; they all have problems. Maybe a problem I haven't taken seriously enough is, "are you employing an analyst or a data scientist?" Perhaps it's conceptually jarring for me to emerge from the cave of code into the brightly lit GUI of Tableau in a way it simply wouldn't be for somebody who didn't identify like I do. Perhaps there is a class of professionals for whom Tableau is a remarkable and powerful tool -- one to be incorporated into their professional toolbox as Python and R are incorporated in to mine.

Meanwhile, I still have to get my work done.


[^beef]: Major Beef No. 2 for you beef counters at home.
[^win]: And let me be frank about this: no thanks.
[^dataexcep]: There are exceptions; regular reporting and dashboards, for instance, should expose their data with the understanding that once it's been vetted and questioned once it probably wont be poked at every single time the dashboard goes out.
[^codeisdata]: Yes it is. If anybody tells you different, they are wrong.
[^rpkg]: You can try and do without packages, but that overlooks a huge amount of very good work that will save you important amounts of time -- if you can just figure out how the f%&$! they work.
[^zambia]: Which was totally a place when I wrote a report about it.
[^r]: Buried deep inside R is the proudly beating heart of an awesome domain-specific language -- but it's buried pretty deep. I find that I haven't been able to divorce myself from using packages; they overcome many of R's built-in shortcomings, like copying huge datasets over and over again. But R has a hideous syntax, and the packages, in their desire to 'fix' the problems inherited from R itself, often implement New and Different operational paradigms, syntax, and assorted nonsense. The result is that R is profoundly hard to share with non-R programmers in a way simply not true of something like Python. More and more, I'm considering that to be an important and crippling flaw.
