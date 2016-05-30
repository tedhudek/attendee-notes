Premise is adding AI/machine learning to clippy (adaptive/contextual help). How could you do that? What would it help?

Change the interface depending on how people are interacting with the product
Change your documentation (or serve your documentation based on that interaction)

A lot of companies are already doing the behavioral profiling — need a way to turn that into docs and leverage that for the docs

Maybe changing the microcopy based on people’s profiles, plug different types of documentation into the contextual help

How do you recognize the patterns? (Neo4j, graph database)—> looks for graphs that repeat in user behavior, and predict potential problems based on that or understand what leads to support problems
—> start with those ones first

Something else that someone has seen —> have modes where the user chooses a mode based on their level of experience, which relies on the user

Specialized AI can be very simple - can just be recommendation engines, or something similar to that
Takes a lot of contextual information and does stuff with it

Could start with user-selected modes and then tack on the AI on top of that

AI implementations vary - some are based on personalization and there is also the realtime aspect from chatbots

Get a different product experience at GoDaddy if you have >6 domains than other people.

choose your own adventure framework to build it up
“If your page looks like this, do this” “if your page looks like this, do this instead”
can also use that to guide people to the right version of their content
bias toward what you believe someone has - can’t automatically assume anything, but can bias toward what you think they need

Write content with personalization in mind even if it’s not there yet technically

That can accommodate personalization of input/scenarios of people’s experiences —> if you’re on a mac, bias toward mac-based instructions

Can’t totally trust signed-in information
If you have a lot of data on users, it gets easier to do this kind of personalization (can build in a feedback loop)

Doing anything with chatbots?
hooking up AI w/ chatbots wasn’t super useful, but were super useful as support systems to guide people through

slackbots come up - 18F has a slackbot for onboarding - more as an agent to get stuff done
https://github.com/18F/dolores-landingham-bot

supervised learning + customer data = trained chatbot so you don’t have to manually convert a KB or docset to support a chatbot

If a chatbot could get you to where you needed to go with the context of how they did that,

open source summarizers to show a summary of an article

Marketing automation - sailthru - logging what you do as a user, does it for other companies that amazon does in-house
personalization

Personalize these items based on what you’ve seen people do in the past? Right now it’s just media and commerce

So many of these things end up in marketing first!
For eCommerce with money the value is clear but there’s a lot of value in documentation too

“If this user is on this URL path or this user ID type, show them this"

Kristof wants to build a toolchain that doesn’t require you to program everything separately — figure out what the patterns are and set reactions in one place.

- as a technical writer you could react to emerging patterns in user behavior and write to support that

The machine learning aspect of AI…
the path one follows to get to help is likely a path that many other people follow to the same thing

clicking help doesn’t automatically route to a search box, but can recommend articles
if you recognize patterns, you can intervene in someone’s workflow

key tech there = collaborative filtering. Watch patterns and identify peer groups

End up on the documentation page and you have to select your product to find where you need to be - but to make recommendations and intervene there is easier.

Personalization works better with login because there’s more consent
As long as it’s in the context of a company that you have a relationship with it’s more the cross-site stuff that’s creepy.

Twitter example, want to customize discoverability of documentation for roles (If you do an internal search for something that has multiple meanings, what are you really looking to find?)

Also can use that to break down silos (search across multiple systems with Elasticsearch)

Hadoop lets you store your log/session data and then find the patterns in it using something else

How people are interacting with everything that you have —> get all the data and look for patterns for specific users

A lot of companies already collect this type of data (e.g., marketing) but may or may not be sharing it more widely.

Getting the data is the first step.

Can get Elastic MapReduce on Amazon easily but harder to start using without data science experience

Google analytics and looking at the web telemetry is one place to start

Cases where you kind of know what you’re looking for but you’re not sure where to look —> that isn’t somewhere that “Bayesian” inferences shine

"Expert systems” to target specific use cases (like medical expert system on the space station)

There are levels of personalization capabilities...

- can I perceive what kind of user I’m working with?
- how interactive are we?

Helpful AI

- shows up when invited
- gives you help when you want it and that helps you
- can’t introduce tips so often
- avoid optimized for first use

Intrusiveness is the danger — when are you no longer a friend?
Danger in AI is that it can mask its benefit

When people access the help, they’re already frustrated —> don’t want it to be too annoying or presumptive because you could FURTHER alienate them.

Ideally take this back to your development team continuously and early on to help improve the UI and help confused users.

Do you (and how do you) treat frustrated users differently?

https://gethuman.com/ is an interesting model because it onboards you with a chatbot to get the information needed for them to handle the call on your behalf.

Summarizers chop up the text based on rules such as:

- take out the first and last sentence of every paragraph since they tend to be most important.
- or looks for the most-commonly occurring subject and focuses more on those ones than others.
