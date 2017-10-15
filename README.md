# Social Network Analysis Sandbox

This is where @aguestuser will put problem sets and toy projects for learning Social Network Analysis as a side project for their work on [LittleSis](https://littlesis.org).

## Texts

### Definitely Reading:

* [Social Network Analysis](https://www.amazon.com/Social-Network-Analysis-John-Scott/dp/1473952123/) by John Scott -- solid intro w/ history of field, treatment of major algorithms, written from perspective of a sociologist mapping corporate power trying to learn the math


### Might read

* [Social Network Analysis: Methods and Applications](https://www.amazon.com/Social-Network-Analysis-Applications-Structural/dp/0521387078/) by Stanley Wasserman -- heavy-on-the-math treatment of SNA methodologies, good to read after the Scott book?
* [Analyzing the Social Web](https://www.amazon.com/Analyzing-Social-Web-Jennifer-Golbeck/dp/0124055311) by Jennifer Goldbeck -- this one is all about mining social media platforms for social network data! we should totally learn how to do this for corporate targets! turn the weapons against their makers!
* [Analyzing Social Networks](https://www.amazon.com/Analyzing-Social-Networks-Stephen-Borgatti/dp/1446247414) by Borgotti, Everett, and Johnson -- this is a captivating book: written by researchers and software developers with a heavy emphasis on how to model graph analysis in computational algorithms. however the software-driven bits seem tightly coupled to an outdated, proprietary graph analysis software tool called UCINET that only runs on Windows. I discarded it for that reason, but maybe a closer look will reveal that the book is more translatable into our context than I ghouth?
* [Understanding Social Networks: Theories, Concepts, and Findings](https://www.amazon.com/Understanding-Social-Networks-Theories-Concepts/dp/0195379470/) by Charles Kadushin -- broad overview for non-mathmatical audience, seems redundant with other choices above, namely the Scott book, which seems better written


## Tech

### graph analysis libraries (python)

* [Graph Tools](https://graph-tool.skewed.de/) super-performant, well-documented, expressive library that can model property graphs (ie: where data is stored on edges)
* [SNAP](http://snap.stanford.edu/) the gold standard for graph analysis in the sciences, also super-perofrmant and well-documented, but does *not* model property graphs

### distributed graph analysis (spark)

**Stub:** found a bunch of links on GraphX and plugins for it, but have to chase them down and add them later -- @aguestuser

### graph databases

* [O'Reilly Graph Databases Book](http://shop.oreilly.com/product/0636920028246.do) -- solid intro to Cypher query language (Neo4J) and graph modeling more generally -- rec'ed by @connorwalsh
