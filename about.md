---
layout: default
---

This site contains [short summaries of papers]({{ "papers/" | relative_url }})
related to what I am working on or that I am thinking about.

The summaries of papers will usually be brief and based on a single quick
skim of the paper.
If you are an author and feel that I misunderstood your paper,
I am happy (eager!) to correct details if you want to get in touch.

## Notes and topics

Inspired by the [Zettelkasten] idea, I recently started writing
[notes]({{ "notes/" | relative_url }})
about concepts that occur in multiple papers
and I link each paper to the relevant notes.

This replaces an earlier plan to create
[mini summaries of research topics]({{"topics/"| relative_url }})
in different areas.
The original plan was that I would break each research topic up
according to some taxonomy and write a little about each sub-topic
and link in the papers that fit that taxonomy.
I found it too hard to maintain this plan:
it is hard to come up with a good taxonomy;
it is hard to figure out where to put a paper when it is the first in some sub-topic;
I am typically only reading some narrow slice of a field skewed by my interest;
I am an outsider/newcomer to the field struggling to make sense of what I am reading
and to find the important papers in a sea of publications

Changing to the "note" format avoids these problems because I try to keep
the notes focussed on a single concept (so there is little need for
organization within notes) and I vigorously cross-link the notes.
Since the organizing principle is links between notes, the structure
evolves organically as I add links and notes: there is no need for me to
create a taxonomy before I even understand the subject.

I will probably delete the "topics" part of this site once I have
created a note for each of the current topics.

## Recommendations for learning a field

This site is the result of my need to learn a new research field
where I am a complete newcomer and don't know the shape of the field:
the important papers, the important research groups/people, the important
concepts.
In fact, I don't even know the terminology and how it is normally used.

I have had to do this several times in my career so I have some
recommendations.

1. If you have a list of papers (e.g., some subset of the papers in this list
   or a list of classic papers in the field), collect all the papers and
   then read them in the order that they were published.
   Reading them in this order helps you understand how the field developed,
   what contribution a paper made to the field, how the terminology and
   notation changed over time, what ideas were once important but now
   seem to be ignored or a bit old-fashioned.
   I find this to be the most satisfying and rewarding order to read papers.

   (As you do this, your interests will evolve and you will find other
   papers and topics that you ought to read.  So you will also have
   to hunt for papers and try to evaluate the importance of papers
   by following the next criteria.)


2. If you do not have a list of papers, the key thing is to create your
   own list.

   Start with the most recent major conference in the field and skim the
   Related Work section of every paper looking for:
   - which authors are frequently cited
   - which papers are referred to as "seminal work" or similar
   - which papers are often cited
   - which other conferences are the important papers published at
   and update your list of papers.[^star-papers]

   At this stage, you will have a list of papers that you think
   might be important.
   Follow up each of these leads to find more papers, conferences and
   authors that you ought to read.
   Try to evaluate the importance of a paper or author by looking at the citation
   count in [Google Scholar](https://scholar.google.com/)
   versus the age of the paper
   and by looking at the related papers.
   Now read a few of the papers and use any new understanding to update
   your list.

   Unfortunately, this will result in you reading the newest papers
   first. Oh well, it's the best you can do...

[^star-papers]:
     If you use [Google Scholar](https://scholar.google.com) to lookup papers,
     it can be handy to "star" papers to keep track of the interesting papers.

I like to print papers so that I can stuff them in my pocket,
read them on the train, underline sections, put questions to myself
in the margins, etc.

After reading each paper, make notes about the paper (maybe a bit like
the notes on this site).
I think it is also a good idea to try to write notes about ideas that span
multiple papers both to reduce redundancy and to encourage you to
identify the key concepts in a field.

Writing notes about papers and concepts forces you to think about how
to explain the material – which is a great way of forcing yourself
to understand it.
It also forces you to practice using any new terminology you find
in the papers.  For example, just what is the difference between
"symbolic evaluation" and "symbolic execution"?
Finally, if you find yourself writing a paper in the field,
then parts of your notes about a concept or a paper can maybe be copied
directly into the paper.
(At least, that is what the [Zettelkasten] advocates claim.)

As you read each paper, be sure to record enough information that you will be
able to find the paper and cite it in the future.  My approach is to get
a BibTeX file for the paper and use a
[script to convert that to
json](https://github.com/alastairreid/RelatedWork/tree/master/_scripts/bib2md.py)
that I include in the summary that I write.  I believe that I could reconstruct
a BibTeX file from that information but I have not yet written the script
to do so. Alternatively, the
[doi](https://en.wikipedia.org/wiki/Digital_object_identifier)
information should be enough.

It is probably a bad idea to copy the content of this site – you will learn
more by trying to write your own summaries and notes.
But, by all means, copy the framework/scripts and, if it is relevant,
my list of interesting papers.


## Building the site

The tooling around this site is pretty simple at the moment: I have repurposed
the Jekyll material from [my website](https://alastairreid.github.io) (which is based on
[Barry Clark's Jekyll Now](https://github.com/barryclark/jekyll-now))
and I have a
[Python script](https://github.com/alastairreid/RelatedWork/tree/master/_scripts/bib2md.py)
that converts BibTeX entries to page templates.
But ideally this would be much more integrated with one or more of the main
research search engines like [Google Scholar](https://scholar.google.com)
– perhaps as some form of overlay over the basic website.

I recently updated the [404 page]({{"404.html"| relative_url }})
based on the awesome glitch effect on the [SeaHorn 404
page](http://seahorn.github.io/404.html)
that is based on [this glitch effect](http://codepen.io/bulby97/pen/fcvay).
This may hurt your eyes.

I have been slowly working on a [clean
rebuild](https://alastairreid.github.io/clean-slate/) of this site based on the
Jekyll default site profile with the minimum number of changes to give it the
important features of this site.

---

[Zettelkasten]: https://zettelkasten.de/posts/zettelkasten-improves-thinking-writing/
