---
ENTRYTYPE: inproceedings
abstract: In this paper, we propose two low-cost and novel branch history buffer handling schemes aiming at skewing the branch prediction accuracy in favor
  of a real-time thread for a soft real-time embedded multithreaded processor. The processor core accommodates two running threads, one with the highest
  priority and the other thread is a background thread, and both threads share the branch predictor. The first scheme uses a 3-bit branch history buffer
  in which the highest priority thread uses the most significant 2 bits to change the prediction state while the background thread uses only the least significant
  2 bits. The second scheme uses the shared 2-bit branch history buffer that implements integer updates for the highest priority thread but fractional updates
  for the background thread in order to achieve relatively higher prediction accuracy in the highest priority thread. The low cost nature of these two schemes,
  particularly in the second scheme, makes them attractive with moderate improvement in the performance of the highest priority thread.
added: 2019-06-01
affiliation: ARM Ltd
ar_shortname: SBAC-PAD 07
authors:
- Emre Özer
- Alastair Reid
- Stuart Biles
booktitle: 19th Symposium on Computer Architecture and High Performance Computing (SBAC-PAD 2007)
day: 24-27
doi: 10.1109/SBAC-PAD.2007.15
layout: paper
location: Gramado, RS, Brazil
month: October
pages: 37-44
publisher: IEEE Computer Society
read: false
readings: []
title: Low-cost techniques for reducing branch context pollution in a soft realtime embedded multithreaded processor
year: 2007
topics:
---

{% include links.html %}
