---
layout: post
title: "Correcting Text Alignment for Gists in Octopress Themes"
date: 2013-08-11 15:19
comments: true
categories: [Code, Web]
---

So I'm setting up my hella sweet Octopress blog and I'm feeling pretty sharp and I decide it's time for a theme. What could be better! Gussy the place up a bit. There are [bunches of themes](https://github.com/imathis/octopress/wiki/3rd-Party-Octopress-Themes) available, so that bit was pretty simple. Installation: boom! Previews: bam! All exactly as easy as advertised. 

To celebrate, I decide to publish my first github gist. 

And all the text aligns center.

...

Okay so I have no idea why anybody would ever, ever do that, but the answer seems to go like so: there's an SCSS template in `sass/parts` called `_article.scss`. It contains a CSS entry, so (many things removed for brevity):

     article{
		.entry-content{
			table{
				background: $color-gray04;
				border: 1px solid $color-gray03;
				border-spacing: 0;
				margin-top: 10px;
				th{
					background: $color-gray03;
					padding: 0 15px;
				}
				td{
					text-align: center;
				}
			}
		}
	}
{:lang="haml"}

That little td definition is the one that gets you, and here's a thing that threw me off for a bit: this same file exists (almost identically) inside `.themes/[Your Theme Name]/sass/parts/` -- and changing the theme-specific file does *not* override the stuff in `[Blog]/sass/parts`. Only tweaking the top-level definiton put my gist back over to the left. 

I'm pretty much a CSS n00b, so it's entirely likely there's something derpy I'm doing/not getting with this. If any Octopress ninjas out in Blogland have a clearer idea of what's going on than I do, _please_... oh wait. This theme doesn't support comments. 

Tweet at me. That's it. [With this handy link](http://www.twitter.com/Gastove)