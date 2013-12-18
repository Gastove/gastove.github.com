Title: Scalatra and Backbone: A Rudimentary Tutorial
Author: Ross Donaldson
Date: 2013-12-17 20:31
Slug: 2013-12-17_scalatra_and_backbone_a_rudimentary
Category:
Tags:
Summary:
status: draft

[Hey hey verbiage. Figure this bit out better. Background.]

Stack:
- Scalatra (Server-side framework)
- Backbone.js (Front-end framework)
- Postgres (Backend DB)
- Squeryl (ORM)
- C3P0 (Connection Pooling)
- Heroku (Hosting)
- git/github (implied)

## Resources
- [Scalatra on Heroku](http://www.scalatra.org/guides/deployment/heroku.html)

## Setup and Init

Phase I: Framework
- Use g8 to setup project framework. (Scalatra docs)
- Do a little tidying up:
-- Move Servlet and Bootstrap out of src/main/scala/com/whatever/hoodly-hoo into src/main/scala (this is purely because it annoys the crap out of me)
- git init (legit)
- Add JettyLauncher and Main Method (in Scalatra on Heroku docs)
- Tweak project/build.scala (in Scalatra on Heroku docs)
- Test in browser (sbt clean compile stage, then fire up sbt and make sure container:start gets you someplace)
- Add Procfile and check for Heroku set-up-correctly-ness with Foreman
- Freshen up Git
- Add to heroku
- BOOM

Phase II: Infrastructure (Setting up Postgres)
- Provision a Postgres DB in Heroku (whee!)
-- Probably already provisioned, needs to be promoted.
-- Gonna need to figure out what you wanna do locally.
- Add deps for Squeryl, C3P0, Postgres to your project/build.scala
- (Note here about % vs %% in sbt deps)


Phase III: Data Model and JSON
