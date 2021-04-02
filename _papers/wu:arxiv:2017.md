---
ENTRYTYPE: misc
added: 2021-04-02
archiveprefix: arXiv
authors:
- Lingfei Wu
- Dashun Wang
- James A. Evans
eprint: '1709.02445'
layout: paper
primaryclass: physics.soc-ph
read: true
readings:
- 2021-04-02
title: 'Large teams have developed science and technology; small teams have disrupted it'
year: 2017
notes:
papers:
---

This paper argues that papers with a small number of authors cause more
disruption (introduce new ideas) than those by large teams while papers by
large teams tend to develop existing (typically recent) ideas.  Interestingly,
authors behaviour changes depending on the team size.  It uses an extensive
data analysis across many different fields and across papers, patents and
software to argue each point: the main argument is in the highly recommended
first 6 pages but the remaining 47 pages have *lots* of graphs, explanation of
the methodology, etc.

*[The same authors published a paper with similar title
and graphs 2 years later in
[Nature](https://doi.org/10.1038/s41586-019-0941-9).
I read and summarized the arXiv version to avoid Nature's paywall.
After I had written this summary, I found that the NSF
[makes a PDF of the Nature article available](https://par.nsf.gov/servlets/purl/10109889).
The main conclusions are the same but diagrams and writing look to be
a bit clearer/sharper so you might want to read the Nature version first.]*

The paper rests on how they decide whether a paper is disruptive or developing
which they illustrate with this rather beautiful visualization of the citation patterns.
(Note: these diagrams are not in the Nature version.)

![1. Disruptive and developmental papers (A-C)]({{site.baseurl}}/images/wu:arxiv:2017-1a.png)

Figures 1(A-C) shows the citation patterns of three papers.
For each paper,
the vertical access is time;
the roots are the papers it cites;
each branch is a papers that cite it;
the length of a branch is the impact of each of those citations.
Each branch curves down and is coloured red if it also cites the
papers cited by the paper or curves up and is coloured green
if it does not cite the citations of the paper.

The intuition behind this is that a green (disruptive) paper like 1A
*eclipses* prior work so the references of a disruptive paper
are not cited so much while a red (developmental) paper like 1B
adds to but does not replace the field so the references of
a developmental paper are also relevant to cite
and a neutral paper like 1C is somewhere in between.

Some of the other things they explore are

- Relationship between funding and disruption.
  They suggest that larger teams (with larger funding) are
  more risk-averse and, in fact, even small teams with funding
  are less disruptive.
  Suggesting either that disruption comes from teams with nothing to lose
  or that funding processes are risk averse or that
  "small teams lock themselves into big team inertia by remaining
  accountable to a funded proposal."

- The patterns they observe are consistent for 90% of the disciplines they
  analyze, but they only analyse journal publications, not conference
  publications.

  > the only consistent exceptions [to the patterns] were for disciplines
  > (e.g., Engineering and Computer and Information Technology) where
  > conference proceedings rather than journal articles are the publishing
  > norm.

- An interesting observation is that the disruptive papers tend to have longer
  roots (cite older papers) while the developmental papers have shorter roots
  (cite newer papers).

  > Larger teams, with more people spanning more dispersed areas, cannot be
  > less aware of older, less popular work than small teams, but they have been
  > systematically less likely to build on it. Indeed, larger teams have been
  > much more likely to target recent, high-impact work as the primary source
  > of their ideas, and this tendency increases monotonically with team size.
  > It follows that large teams have received more of their citations rapidly,
  > as their work is immediately relevant to more contemporaries whose ideas
  > they develop.  Conversely, smaller teams experience a much longer citation
  > delay, with an average Sleeping Beauty Index for solo and two-person
  > research teams four times that of tenperson teams (Fig. 3D).

- The sleeping beauty index: papers that are ignored for some
  time before their citation rate starts to grow.
  (Higher for disruptive papers. Developmental papers tend to
  grow citations linearly for first 10-20 years.)

- Impact on breadth of ideas: small, broad teams win over large teams.

There is a lot more in the first six pages and the remaining 47 pages give detail,
lots of graphs, methodology and other insights.

{% include links.html %}
