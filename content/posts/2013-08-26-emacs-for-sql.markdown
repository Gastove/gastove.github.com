Title: Setting up Emacs Prelude for Multiple SQL Databases and Query Development
Author: Ross M. Donaldson
Date: 2013-08-26
Slug: 2013-08-26_emacs_prelude_for_sql
Tags: Tools, SQL, emacs, GTD
Category: Data Science
Summary: Wiring up SQL to Emacs Prelude

---
layout: post
title: "Setting up Emacs Prelude for Multiple SQL Databases and Query Development"
date: 2013-08-26 20:47
comments: true
published: true
categories:
---
Ah, emacs. What can't you do?

...actually, that's the problem. Emacs, for all its splendor, can be an infinite rabbit hole of customization, modification, tweaking, scripting, and parens. I recently discovered [Emacs Prelude](www.github.com/bbatsov/prelude), and I recommend it heartily. It does, for the most part, what it says on the tin: "The final product offers an easy to use Emacs configuration for Emacs newcomers and lots of additional power for Emacs power users." Check and check.

That still leaves some customization to be done, and a particularly common use case in my work is SQL query development, often in the context of embedded SQL within an automated reporting framework. Developing queries with SQL GUIs like MySQL WorkBench and Sequel Pro is lovely... but I don't always have access to them, and copy-pasting queries from one editor to another is a lovely way to introduce bizarre characters into an otherwise pristine query. (And who doesn't love debugging those!) A better answer would be to manipulate embedded SQL in-place -- in this case, from within Emacs. Fortunately, this isn't hard.

<!--more-->

Emacs has a set of built-in protocols, accessible via `sql-*` (e.g., `sql-mysql`). They work beautifully, allowing a parallel SQL 'interactive' (or 'SQLi') buffer that's effectively an augmented SQL CLI. The augmentation allows you to ship SQL from the buffer you're editing in to the SQLi buffer for evaluation using one of three basic approaches:

* `sql-send-buffer` -- fine for one-off query development but otherwise a little too broad
* `sql-send-paragraph` -- better; tries to auto-detect a delimited unit of SQL, but doesn't always work
* `sql-send-region` -- ideal. Ship an arbitrary region in to the SQLi buffer

The last issue to tackle, then, is this: `sql-*` mode can't autoload your local DB configs. Hooray! If you have a `my.conf` you're particularly proud of, it wont avail you here - instead, a command like `sql-mysql` will leave you entering in your credentials over and over again. There are some [very good](http://stackoverflow.com/questions/5734965/how-can-i-get-emacs-sql-mode-to-use-the-mysql-config-file-my-cnf) StackOverflow posts about getting around, this, but they all miss two points: I really don't want to have to store my DB credentials in plain text; I have to connect to like twelve different databases.

My solution (written up in my Prelude `custom.el`) looks like so:

```cl
(setq sql-connection-alist
      '((db01
         (sql-product 'mysql)
         (sql-server my-server-name)
         (sql-user (getenv "MYSQL_USER"))
         (sql-password (getenv "MYSQL_PASSWORD"))
         (sql-database "wordace")
         (sql-port 3306))
        (db02
         (sql-product 'mysql)
         (sql-server my-other-server-name)
         (sql-user (getenv "MYSQL_USER"))
         (sql-password (getenv "MYSQL_PASSWORD"))
         (sql-database "")
         (sql-port 3306))))

(defun sql-connect-preset (name)
  "Connect to a predefined SQL connection listed in `sql-connection-alist'"
  (eval `(let ,(cdr (assoc name sql-connection-alist))
    (flet ((sql-get-login (&rest what)))
      (sql-product-interactive sql-product)))))

;; Function to load a DB based on its short name
(defun sql-connect-preset-by-name (name)
  "Connect to a DB by entering it's short name"
  (interactive "DB Name: ")
  (sql-connect-preset 'name))

(global-set-key (kbd "M-s q") 'sql-connect-preset-by-name) ; Connect to a db preset by name
```

This pleases the hell out of me. Hitting `M-s q` prompts me for a server short-name (in this example, 'db01' or 'db02'), and loads my credentials out of environment variables where they're safe and sound. Win!
