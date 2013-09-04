---
layout: post
title: "Android Shape Password Permutations"
date: 2013-09-03 16:03
comments: true
published: false
categories: Scala
---

My friend Steve recently posed an interesting challenge to me:

"i thought of it on the plane back from vermont, basically, calculating the potential passwords possible on an android phone."

Very interesting. The full problem statement goes a little like this:

* An Android Password has nine available nodes in a 3x3 grid.
* A valid password has no fewer than four and no more than nine nodes.
* A node can only connect to a "reachable" node -- that is, from the top left corner, your next move cannot be to the bottom right corner.

The rules of reach-ability are by far the trickiest bit of this. How do you tell a node which Other Node it can get to? Particularly without my personal pet problem: overflowing the heap. (Or the stack. Or both.)

Steve is one of the smartest computer scientists I know, has his Ph.D. , and deeply groks graph theory. I'm a musician-turned-hacker with too much free time and a dodgy understanding of the classic algorithms. His an my approaches? Likely to look very different. Here, I'll detail mine.

I started with the thought that the smallest conceptual unit here is a Node. Nodes build in to a Path. A Node should know its context, but a Path should know the rules of path-building -- including exceptions to the standard rules. Armed with this idea, I wrote two hundred-odd lines of Scala and melted the heap.

Fantastic.

As a programmer I operate in much the same way I do as a writer: when I'm writing serious essays, I write down *everything*, censoring as little as possible, just slathering the page in words. As I write more and more and more, I begin to perceive the underlying structure of what I'm up to -- and it's a structure I have to find a way to materialize outside my own head in order to understand it clearly. Then there's A Moment of Clarity, a click, when things suddenly drop in to place and I start removing chaff in huge chunks, carving away at the mass I created to leave an essential, spare Thing.

So with writing, so with my code. I wrote vastly more code than I needed, refactored, wrote more code, got it compiling, branched, and wrote more code until finally I noticed something incredibly simple:

One node can always reach any other node as long as you add the node that's "in the way" to the Path.

When I'm coding, I call this moment, "the Collapse". It's the point at which I can suddenly see the underlying structure I've been feeling out and I can work to realize it, when I can stop laying down material and start carving away at it. The above let me peel away more than half the code I'd put in place, and while the result wasn't bug free (editing still required), it was A) comprehensible, B) terse, C) fixable, and D) kinda elegant. It's this last that often is my surest indicator I'm on the right path -- when things stop looking less _eugh_ and more _oooh!_

The final product needs some space to run; I had planned it as an interactive demo on my web page, but it uses far more RAM than Heroku will allow me*. The code lives in its original state in my repo for gastove.com, but I also pulled it all together in a run-able Gist, like so:

{% gist 6429057 $}

Now, we just have to see how Steve solved it. Probably lasers.

* Which is not saying much. Heroku gives you 512mb per 1x Dyno. Feh.
