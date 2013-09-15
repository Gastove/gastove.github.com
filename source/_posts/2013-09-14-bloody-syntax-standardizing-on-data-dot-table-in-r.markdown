---
layout: post
title: "Bloody Syntax: Standardizing on data.table in R"
date: 2013-09-14 11:54
comments: true
categories:
---

Here are some things:

In our familiar data.frame, the fastest subset we've got goes something like this:

df = df[df$foo == 'a']

To subset by row and , say, a couple columns:

df = df[df$foo == 'a', c('col1', 'col2', 'col3')]

Hillrious:
dt = dt[foo == 'a', list(col1, col2, col3)]


* Evaluating symbols within subset without having to use `expression` and `eval`
