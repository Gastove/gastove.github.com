---
layout: post
title: "Thoughts on this Site So Far"
date: "2013-08-11 16:58"
comments: true
categories: [Code, Thoughts]
published: false
---

Huh. Okay. This... this kinda seems to be working. So far, this has been an interesting project. Over the last two days, I've spun up a personal web page and a blog, both from code (that is, not using WYSIWYG editors or 3rd Party stuff). I'm using what I can only describe as an Ecclectic Blend of tools -- something I have mixed feelings about. Lets do a little review, after the cut:

<!--more-->

#### Scalatra

My main site is written in Scala, hosted on Heroku. In all, hosting has been one of the easiest parts; Heroku has some special configuration requirements, but  provides very good, accurate docs, and setup is mostly a breeze. There are, it turns out, several web frameworks for Scala -- most notably [Lift](http://liftweb.net/), [Play](http://www.playframework.com/), and [Scalatra](www.scalatra.org). I've gone with the last of these; so far, it's been easy as can be. Scalatra is intuitive, plays well with Heroku, and is even decently well documented. HTML Templating is handled with Scalate.

Ah. Scalate.

Scalate is the main game in town for Scala HTML templates, as near as I can tell. On the up side, it's powerful and fast and pretty robust. It supports more templating choices than I'd actually care to make, and that might be the down side. For mostly arbitrary reasons, I got going with Jade -- which is a terse form of Scaml, which in turn is Scala Haml. 

Perhaps you've already intuited the problem. There are a bunch of templating choices, and I picked the one that's the most abstreuse, the least interoperable, and the hardest to find support for. Scalatra doesn't _actually_ support all of Jade (*cough* inheritance), so finding clear help for Scalatra Jade vs. Jade Itsownself is kind of a mess. 

All that said: Jade is both easy and fast to write, *very* DRY, and about as powerful as you could want. I've made my bed, and now I'll lay in it -- and I don't think that's too bad.

#### Octopress

I have fallen almost instantly in love with [Octopress](http://octopress.org/), a blogging framework that defaults to publishing on Github Pages (as it should be). So far it has been an absolute pleasure to use, though I cannot say the same for most of the themes I've tried. Now: fussing and whining about themes is maybe a dodgy proposition for a guy who couldn't write one to save himself from sharks. But then, that's why I went hunting for third party Octopress themes in the first place. There are [a lot of them](https://github.com/imathis/octopress/wiki/3rd-Party-Octopress-Themes). They feature truly beautiful page stylings and truly peculiar CSS choices -- like defaulting to centering the text inside a code block. That's right. Centered. Code. 

Beyond some CSS-hackery to get code aligned correctly, my only other real trick was setting up syntax highlighting. (Octopress comes with Solar built-in, but I'm not, uh, a fan of Solar.) Thanks to some [very good directions](http://blog.alestanis.com/2013/02/04/octopress-and-the-twilight-color-scheme/), getting Twilight going didn't take long at all. And now, I get code blocks like this:

       def fizzbuzz:
       	   for x in range(0, 101):
	       	 fizzbuzz = ""
		 	    if x % 3 == 0:
			       	   fizzbuzz += "fizz"
				   	       if x % 5 == 0:
					       	      fuzzbuzz += "buzz"
						      	       	  print fizzbuzz
{:lang="python"}

Being the sort of doofus I am, I got Octopress working, then trotted out to find an emacs plugin to run it. Octopress is a framework that wraps the thorny-but-powerfull Jekyll blogging engine; it figures the emacs package would be [Hyde](https://github.com/nibrahim/Hyde). Beyond fussing with some of the `.el`s to update Hyde's new post boilerplate, I've found it to be just as easy to use as most of the rest of this stuff.

#### In Conclusion

The web is a lovely place, with a remarkable number of very cool pieces that don't take long to pull together. It takes a little time, sure, and some command line know-how -- but I know have a web presence that makes me smile. 
