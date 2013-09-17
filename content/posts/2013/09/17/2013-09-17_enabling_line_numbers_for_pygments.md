Title: Enabling Line Numbers for Pygments Code Blocks on Pelican
Author: Ross Donaldson
Date: 2013-09-17 09:38
Slug: 2013-09-17_enabling_line_numbers_for_pygments
Category:
Tags:
Summary:


I recently migrated this blog from Octopress over to Pelican; in all, it was a pretty simple process. With a moment of Googling, you can have your pick of exhaustive tutorials on how to do this well -- or, you can do what I did and Just Wing It. This is not actually a post about how to migrate.

This is a post about filling in a little gap in the Internet's Knowledge about how to use Pelican well for code blogs. Specifically: code blocks.

Pelican will tell you straight out of the gate that the excellent [Pygments](http://pygments.org/) package is baked right in; this is, more or less, good news. Where things get vague is on the question of configuration. `Pygments`, after all, is sort of a simple beast; it eats chunks of code and spits out nicely tagged HTML. It can do a lot of things, if you can just figure out how to pass it a message. On this point, the Pelican docs are woefully vague.

I'll spare you the tale of how I finally figured this out. Instead, here's what you need to know:

1. Unless you're some sort of code-masochist, you're likely writing your documents in some sort of markdown format -- either reStructured Text (`.rst`) or Markdown itself (`.md` or `.markdown`, among others). Personally, I'm using Markdown.
2. This part, Pelican will tell you: In Pelican, Markdown support is provided by the Python [Markdown](https://pypi.python.org/pypi/Markdown) package.[^md] This has to be installed separately, but comes with a lot of good stuff baked in.
3. This part, Pelican omits: much of the good stuff in `Markdown` has to be explicitly activated. Ruh-roh.
4. Markdown is what handles sending code in to `Pygments`. (Can you see where this is headed?)
5. So, if you want some Extra Awesomesauce in your codeblocks, you're gonna have to enable some stuff.

This is where things get a touch stupid. It turns out there's a ridiculous number of ways to indicate to `Markdown` that a codeblock needs working over. You can use fences (a string of "~~~~" or "****"); you can open and close with the triple-backtick (` ```scala println("Hello World")``` `); you can use a system of indents and open symbols.

This last one, it turns out, is what we want. `Markdown` supports an extension called `codehilite`; `codehilite` uses a different syntax, but allows (through syntax alone) arguments to be passed in to `Pygments` -- arguments like line numbers. So this:

```markdown
```python
def foo():
	print "Bar!"
```
```
changes to this:

```markdown

	#!python
    def foo():
    	print "Bar!"
```
which outputs this (!!!):

	#!python
    def foo():
    	print "Bar!"

Do note: in the above Markdown sample, there's a newline at the top of the snippet; this is mandatory, as are the indents. But you know what? I can live with this. If you look at the source of the page, you'll also see that the block gets put into a table with a `codehilite` class, making it exceptionally style-able. Win!

[^md]: Note: I'll differentiate syntactically between Markdown the language (normal font) and `Markdown` the python package (code).
