Title: Bloody Syntax: Standardizing on `data.table` in R
Author: Ross M. Donaldson
Date: 2013-09-14
Slug: 2013-09-14_bloody_syntax
Tags: rstats, data.table, standards, data science
Category: Data Science
Summary: `data.frame` is R-standard, and it's great -- like a happy little database table right there in your R environment. But it doesn't scale well with data.
draft: True

The amount of data in my work, like so many things, creeps. I show a chart of five things, people ask for the other six. I show two weeks of history, I'm asked for four more. I instrument a feature and then it's deployed on six new platforms and how's it performing, for all 11 things, with six weeks of history?

There's plenty of good news. Conceptually, processing two gigabytes of data isn't any different than processing one; doubling the amount of history displayed in a chart raises questions of clarity and data display, but on its face, little else. With... one or two exceptions, all of which have to do with performance. This bites you from two places:

1. The Data Store: unless you're working with something like Hadoop, it's unlikely you'll be able to do much cleanup on your data before it leaves the datastore. MySQL lacks... basically everything you could ever want, and probably can't perform meaningful aggregations in MySQL anyways. The latest version of Hive supports windowing functions, which can -- broadly speaking -- be used for outlier cleanup. Me personally? I'm not on the latest version. Conclusion: data must be aggregated after the dataset is pulled.
2. Development: do you work in R? I sure do. Did you know that R can't think about anything it can't hold in active memory? No paging, cool as paging is, and object serialization can, frankly, be a pain in the arse. A cool side-effect of R's memory limit is that there's only one R Session process, and _that_ process is limited by system architecture. A 32-bit system can only allocate four-gigabytes-ish of memory, minus whatever the OS itself uses (maybe up to a gig?). Now, suddenly, you have a maximum total workspace for all objects and processes of... about three gigabytes. It's amazing how fast that goes away.

So! Time to crunch a file that occupies 1.2gb on disk. Many R operations -- especially those on data.frames -- create full copies of the source data as they act on them. This is a pernicious problem; data frames are ubiquitous, and incredibly useful. For instance: much as I love [plyr](http://plyr.had.co.nz/), memory efficient... it is not, especially if you want to parallelize the operation across more than one processor core. Now what do you do?

My answer is [data.table](http://datatable.r-forge.r-project.org/). Let's start with some good news:

1. `data.table` is fast. I wont reproduce the timing tables from the manual, but the web page asserts: 10+ times faster than `tapply()`; 100+ times faster than `==`; 500+ times faster than `DF[i,j]<-v alue`. So far, in terms of speed, it's everything I've ever dreamed of and a bag of chips.
2. It's gentler, active-memory-wise. Many `data.table` operations are optimized to act _on the extant object_ rather than by copying it and modifying the copy. Many `data.table` operations return a new, updated version of the same table. This is very good.
3. `data.table` _extends_ `data.frame`. So, you can use a `data.table` approximately anywhere you can use a `data.frame`.

Let's dwell on that last one for a moment. `data.table` is nice because it gives you exceptionally brisk versions of many of your favorite `data.frame` operations -- like `summary`. `subset` is implemented for `data.table`, that's nice. But if you're like me and write functions that ingest `data.frames`, you're in for a little heartache.

Take subsetting. In a `data.frame`, you might do something like `df2 <- df[df$foo == 'a', ]` -- or, to go by rows and columns, `df2 <- df[df$foo == 'a', c('col1', 'col2')]`. This metaphor is familiar to R; first, we evaluate true/false on all the rows, then we return all the rows that evaluate true, subsetted by a vector of quoted column names. But in a `data.table`, things fly a little different: first we set a `key`, and the `data.table` sorts itself by that key. Then, we pass an expression:

```r
setkey(dt, 'foo')
dt2 <- dt[foo == 'a', list(col1, col2)]
```

`data.table` documentation refers to this as `dt[i, j]` syntax; both `i` and `j` are full-blown expressions, evaluated at execution. Behavior can be problematic:

```r
dt[dt$foo == 'a'] # Returns exactly what you'd expect -- rows where dt$foo == 'a' evaluates to `TRUE`
dt[dt$foo == 'a', ] # Also fine!
dt[foo == 'a', 'bar'] # Returns... 'bar'! The string literal, 'bar'. Huzzah.
```

So that's a mess, especially if you're modifying an existing subsetting operation. The flip side:

```r
# Subsetting by variable evaluation, the data.frame way:
cond1 <- expression(df$foo == var1)
cond2 <- expression(df$bar == var2)
df2 <- df[eval(cond1) & eval(cond2), ]

# The data.table way
dt2 <- dt[foo == var1 & bar == var2]
```

This is the advantage of `i` and `j` being expressions already -- you can simply put everything in place, variables and all, and it evaluates.

Assigning new columns is where things really get good, but also... weird looking.

```r
# Assign a single new column
dt[, new.col := mean(col1)]

# Multiple assigns at once
dt[
,
':='(
    new.col.1 = val1,
    new.col.2 = val2
    )
]

# And the coup de grace, assign with aggregate, followed by merge on keys:
dt[
,
':='(
    new.col.1 = sum(col1),
    new.col.2 = mean(col2)
    )
by=list(col1, col2)
]
```

You want a fast merge? Holy shit: `dt1[dt2]` will join on the keys of each `data.table`, and it will do it very fast (this is called `J()` in dt-parlance). Of course, both `data.table`s need their keys set, and new `data.table`s don't emerge from aggregation keyed. You can also do remarkably fast time series joins like this, but... well, that brings me to the part I really dislike:

The syntax of `data.table` looks nothing like the syntax of anything else in R -- a problem not aided by the extreme heterogeneity of the entire 3rd Party package ecosystem. Everybody has their own notion of how a particular computation should be executed, which destroys conceptual portability. Once you finally get your brain around the `apply` family of methods, you get to wrap your brain around `plyr`; once you grok `plyr`, you'll be delighted to learn that nothing you know transfers to `data.table`. It becomes somewhat mandatory to get to know the underpinnings of each set of functions; `plyr`, for instance, is preferable to me for CPU-intensive tasks because it can be easily parallelized, while `data.table` is the clear winner for memory-bound tasks. Circling properly back to `data.table`, one gets the feeling that there's some truly blackbelt stuff to be done if you can just figure out _how_. For instance: `dt[J()][i, j][i, mult='first'][j=list(a, b, `:=`(new1 = expr1, new2:= expr2)), roll=T]` is, as near as I can tell, entirely legal -- each processed `data.table` passing directly into the next set of calls. As a Scala developer, I get this; as somebody whose spent time trying to figure it out, I've still got no idea what `roll` really does, or why I'd want to use it.

In conclusion: `data.tables`: unbearably good for what they're good for, if you can ever figure out how to do it.
