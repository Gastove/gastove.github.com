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
- Set up the code for database connections so that Squeryl methods can be mixed in to Servlets
- Stop here for some Real Talk about Postgres

SO: You're gonna run a remote Postgres DB on Heroku. That's a superb idea. Here's the question: what do you do about local development? You can either:
A) Run a local Postgres instance and connect to it. This means setting up environment switches so that your app does the right thing depending on where it runs.
B) Connect directly to your remote Postgres instance, but use a dev DB instead of Prod (something to decouple concerns).

I say: absolutely do A. Particularly simple is a one-two punch of a Heroku environment variable -- mine is called `DEVSITE` -- with Scalatras `context.setInitParameters`.

### Punch One
The Heroku toolbelt comes with a dandy little tool called Foreman. While Foreman isn't perfect (it can be... a bit of a pain in the butt for things like automatic code reloading for your Scala code), it does two things very well: it launches your app precisely as Heroku will; it automatically loads in a .env file from the root of your app's file structure. Boom. Credentials, `DEVSITE` flags, everything can go in there, happy as can be.

### Punch Two
Unlike a Java app, which handles configs in XML, Scalatra uses some wizardry to transfer configuration back in to itself, all in Scala. (Srsly, thanks for that one guys.) In particular, we gain use of the `ScalatraBootstrap` file -- which is already calling our database init and destroy methods. The aforementioned `context.setInitParameters` can be used to set the Scalatra environment to whatever you like; if it's set to any value that starts with the string 'dev', Scalatra's built-in `isDevelopmentMode` function returns true. Simple!

Continuing along, this means we're going to:
- Install Postgres locally
- Hardcode local Postgres configs so we can make sure we're connecting/reading/writing
-- This means taking a detour through setting up a very basic Squeryl schema and data model
- Setup a .env file to contain our local Postgres configs, and a `DEVSITE=True` flag
- Remove hardcoded configs, replace with reading configs from the environment
- Give configs an `isDevelopmentMode` switch to toggle between dev and prod credentials.
- Go eat some chocolate or something. Good job!

Phase III: Data Model and JSON
