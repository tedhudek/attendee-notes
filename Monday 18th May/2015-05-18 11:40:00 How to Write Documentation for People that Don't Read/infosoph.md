How to Write Documentation for People that Don't Read
=====================================================

People Don't Read
-----------------

- People aren't reading your docs because no one reads anything on the internet
- People read left to right, top to bottom (F-shape)
    - lots of text is just ignored
- They look at 
    - meaningful text and images
    - start of paragraphs
    - bullets
    - links, bold, etc
- not
    - big blocks of text 

- plain unformatted text
    - hard to scan
- Ads in docs
    - people skip highlighted sections because they look like ads 
- Avoid text that's too wide
    - 65-90 words per line
- Provide a good "Information Scent" or put everything together
    - make keywords prominent by location or size
- Break up content
    - ordered sections 
- Use a Table of Contents

Users are bad at search
-----------------------

- provide text that includes variants of natural language questions
    - look at search logs
    - look at support requests
    - use verbs that correspond to user's mental model
        - it's ok to have multiple listings that link to the same page

People don't look at text surrounding code
------------------------------------------

- they just copy paste the code
- test your copy/paste
- provide contextual information in code comments
- pull user info into snippets (API Key, etc)
- avoid obvious pitfalls (picking up a bash $ in copy/paste)

Not your docs
-------------

- People google error messages
    - Put exact text in docs for common errors
    - Improve error messages
        - Omitted something? Tell them to include.
        - Invalid paramter? Tell them it's invalid.
- Go out and fix things where users are (stack overflow, forums, etc)
    - Clean up people's questions
    - answer them
- Avoid putting things behind a login wall
- Don't put your doc in PDFs (google doesn't index well)
- Don't let content farms eat your lunch (e.g. wikiHow)
- URL should describe the content
- Every page is a landing page
- Your docs should **always win**

Luke Gaudreau <luke@infosoph.org>
