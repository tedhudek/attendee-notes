Tim Arnold, SAS institute

Put math on the web last year or so? make an image of it and put it in your HTML that way

Need it to be accessible and visible on the web

Real-live accessible math docs

SVG to zoom the equation for low vision

MathML/MathSpeak to support screen readers and blind people

MathML is an XML-type language

MathSpeak leverages ARIA

MathJax is a JS library you can add to your HTML

Way it works in practice

- writers write in MathML or LaTeX
- readers read using browsers and screen readers
- producers use
    - SVG + ARIA + MathSpeak
    - MathML + MathJax to support what the browser or screenreader can’t pick up

MathJax looks for whether it’s getting LateX or MathML, and returns MathML or SVG or Mathspeak

gives you all the pieces you need to make accessible docs with math in them

sighted person sees the SVG

blind person hears the MathSpeak

if the MathSpeak doesn’t work for some reason, pulls up a supplemental page with MathML and LaTeX source
