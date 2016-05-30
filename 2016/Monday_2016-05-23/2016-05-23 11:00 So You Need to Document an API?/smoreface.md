Allison Reinheim Moore, MongoDB, @schmalliso

Information architect and technical writer. Title is “Software Engineer” tho. Previously API docs at Oracle.

APIs are sets of requirements that govern how one application can talk to another. Brian Proffitt, ReadWrite.

RESTful APIs - use endpoints

REST is an architectural style for API building. Most APIs are RESTful, rather than REST compliant. They generally:
- communicate over HTTP
- use GET, POST, PUT, DELETE HTTP verbs

When you open a webpage, GET HTTP

When you submit a form, POST HTTP

Reference documentation contains these things:
* Endpoint
* Arguments - things you can submit to the API
* Example Request
* Example Response

Reference documentation for APIs includes all of the endpoints, assets, resources, units and forms and response codes and errors.

For APIs, view is often that reference documentation is enough, but she thinks NOPE
- Are the API users different from your regular users? Often, there is no overlap between the two.
- What are your user’s motivations? Is your API mission-critical? This can inform the tone you write and how much you include in “MVP docs” for the product.
- What do people want to do with your API?
- What programming languages are popular among your users? You need to know this to provide helpful and useful code examples for your users.

What does the API do?
- why does this API exist? what does the API let people do?
- How does the API relate to other APIs in your organization?
    - can help users find the APIs that they want to use
- Getting authentication to work
    - access / authentication mechanisms / credential
    - this can be rather opaque if just reference docs

Where do you come in? (as a technical writer)
- What are you responsible for? What are the API developers responsible for?
- Who will be writing the code? (examples)
- How are you going to handle versioning? Is the API going to be versioned? then the docs will need versions, and that could inform how you design the docs.
- Who is going to review what you write?

Concepts to cover
- API call pattern
- Common URI patterns
- Asset descriptions (and how they interact)
- Words and what they mean
    - **sometimes the words that make sense to your organization internally are not the words that make sense to the world**
    - or things that are ambiguous to the world (what’s an account?)

If you’re only going to write one tutorial, write the one that talks about how to authenticate to your API

curl is a command line tool for writing requests against a web server. if you only provide one language, curl is the way to go

Production options:

- Do you want to use the same tool as your current docs? if you’re not using sphinx now, you want to do something else?
- People writing API docs and product docs might not be the same group so using the same tool doesn’t matter as much
- Using a tool that is not well-suited to a use case is crappy - which one sucks more?
    - using tools that aren’t well-suited vs using multiple tools

- Sphinx
    - build HTML, PDF, ePub and a handful more from one feature-ridden source
    - Sphinx extension for API documentation
    - covers reference, task, and concept
- Slate
    - Open source
    - Stripe-style API reference output
    - Markdown backbone
    - supports code samples in multiple languages
    - covers only reference
- MadCap Flare
    - 1 page per endpoint
    - Linking within flare pages was not ideal.
    - Use table snippets for parameters/responses + conditions for whether or not they appear
    - Figure out syntax highlighting for code blocks…
