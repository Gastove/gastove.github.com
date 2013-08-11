---
layout: post
title: "Pure Show-And-Tell: My First Gist"
date: 2013-08-11 10:53
comments: true
categories: [Code]
---

And now, a barefaced excuse to muck about with Octopress markdown and plugins. Presenting: my first gist. Do you care? The whole works (and some verbiage) after the cut.

<!--more-->

While ambling about the internet trying to style my schamncy new web page, I did two things, one clever and one not: 

* **Clever**: I realized I didn't want to write my own CSS sheets, because fuck that noise.
* **Not-So-Much**: I forgot about Twitter Bootstrap. 

I found the pleasing, if peculiar, [Skeleton.css](www.getskeleton.com) -- which is nice looking and open source and free, and rescales (reasonably) well on mobile. Only problem: the provided page template is in straight HTML, and I'm writing in Scalate's implementation of Jade (itself a reduction of Scaml, which is Scala Haml. Oye.) So, I re-wrote the thing. Maybe this will help another person, ever? (Yeah, I think it's a funny line too.)

###The Gist###
{% gist 6201942 %}

