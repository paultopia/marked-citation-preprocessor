A simple preprocessor to use with [Marked2](https://marked2app.com/) to get paths to citation files right based on relative files in pandoc metadata. 

e.g., if you have a markdown file like this: 

```
---
title: "My Awesome Research Paper"
bibliography: bib-csl.json
---

Yadda yadda yadda [@somecite].  Yadda.  Yeah.

```

where bib-csl.json has your references (could also be a bibtex file or whev, but I like CSL json), and you're using pandoc with pandoc-citeproc as a custom processor, and bib-csl.json is in the same directory as your markdown file.  USUALLY, Marked2 can't actually work with this, because it doesn't run from the same working directory as the one the file is in, so you'd have to write in an absolute path to your citation file.  That's bad and annoying.

Then adding this python script in as a preprocessor in Marked will fix the paths, so that pandoc can find the bibliography.
