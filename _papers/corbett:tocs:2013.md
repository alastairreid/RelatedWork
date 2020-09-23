---
ENTRYTYPE: article
added: 2020-09-22
address: New York, NY, USA
articleno: '8'
authors:
- James C. Corbett
- Jeffrey Dean
- Michael Epstein
- Andrew Fikes
- Christopher Frost
- J. J. Furman
- Sanjay Ghemawat
- Andrey Gubarev
- Christopher Heiser
- Peter Hochschild
- Wilson C. Hsieh
- Sebastian Kanthak
- Eugene Kogan
- Hongyi Li
- Alexander Lloyd
- Sergey Melnik
- David Mwaura
- David Nagle
- Sean Quinlan
- Rajesh Rao
- Lindsay Rolig
- Yasushi Saito
- Michal Szymaniak
- Christopher Taylor
- Ruth Wang
- Dale Woodford
doi: 10.1145/2491245
issn: 0734-2071
issue_date: August 2013
journal: ACM Trans. Comput. Syst.
keywords: Distributed databases, transactions, replication, time management, concurrency control
layout: paper
link: https://doi.org/10.1145/2491245
month: August
number: '3'
numpages: '22'
publisher: Association for Computing Machinery
read: true
readings:
- 2020-09-21
title: "Spanner: Google's globally distributed database"
url: https://doi.org/10.1145/2491245
volume: '31'
year: 2013
notes:
- google
- Paxos
papers:
- chang:tocs:2012
---

Spanner is a scalable, globally-distributed, temporal database that shards data
across many [Paxos] instances.  It features automatic failover, resharding and
migration.
Although not explicitly stated, it seems to be a replacement for Bigtable
([chang:tocs:2012]) and Megastore.
One of the early clients was to support F1: an ads database.

Spanner consists of something close to a temporal relational database,
layered on top of a temporal key-value store, made robust against failure
using [Paxos] and relying on "TrueTime" to keep global datacenters synchronized
and allow global serialization of all transactions.

"TrueTime" is a time service that provides time intervals that are guaranteed
to be globally valid.
This is implemented using a combination of GPS and atomic clocks.
The atomic clocks are referred to as "Armageddon masters" and serve mostly as
a backup in case GPS fails.

The paper puts a lot of emphasis on the importance of TrueTime

> As a community, we should no longer depend on loosely synchronized clocks and
> weak time APIs in designing distributed algorithms.

{% include links.html %}
