# So You Need to Document an API? - Allison Reinheimer Moore
@schmalliso

## A very short intro to APIs

"A set of requirements that govern how one application can talk to another" - Get source from slide

Anatomy of a RESTful API

 - REST: an architectural stule. Most REST APIs are actually RESTful (doesn't fill **All** requirements)
 - Typically:
   - Communicate over HTTP
   - Use the GET, POST, PUT, DELETE, HTTP verbs.


Examples, pull from slides.

## Bonus Preamble

Types of Documentation

**Conceptual**

 Really wordy, talks about how things work and interconnect, what can you do generally, common patterns.

**Tutorial**

 Step by Step guides

**Reference**

  What are the endpoints, parameters, resources, units, etc. The nitty gritty.

## Takes Stock

**Questions**

Users:

 - Who are your users?
 - What are your users' *motivations*?
   - changes tone
 - What do people *want to do* with your API?
 - What *programming languages* are popular among your users?

What does the API do?

 - What does the API *let people do*. Why did you make it?
 - How does this API *relate* to other APIs?
 - Access / *authentication mechanisms* / Something else, pull from slide

Where do you come in?:

 - What are you responsible for? What are the API developers responsible for?
   - How do you divide responsibility? Who makes what?
 - Who's writing the code, code examples in languages?
 - How are you going to handle *versioning*?
   - Will the API be versioned?
   - If so, will the docs be versioned?
 - Who's going to review what you write?

## Sorting it out

Concepts to Cover:

 - API Call pattern
 - Common URI parameters
 - Asses descriptions (and how they interact)
 - words and what they mean
   - **The words that make sense internally to your organization to not always make sense to the rest of the world**

Example API Call Format Slide - pull the slide for notes.

Quote from Twitter on API documentation... so bad they downloaded a WP plugin that used it and read the source code. Pull quote from Slide.

Example on how to authenticate with OAuth - pull from slide.

Endpoint references - pull from slides.

## MadCap Flare

 - 1 page per endpoint.
 - use table snippets for parameters / responses + conditions for whether they appear.
 - figure out syntax highlighting for codeblocks.
 