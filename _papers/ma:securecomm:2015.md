---
ENTRYTYPE: inproceedings
abstract: Concolic testing is widely regarded as the state-of-the-art technique in dynamic discovering and analyzing trigger-based behavior in software
  programs. It uses symbolic execution and an automatic theorem prover to generate new concrete test cases to maximize code coverage for scenarios like
  software verification and malware analysis. While malicious developers usually try their best to hide malicious executions, there are also circumstances
  in which legitimate reasons are presented for a program to conceal trigger-based conditions and the corresponding behavior, which leads to the demand
  of control flow obfuscation techniques. We propose a novel control flow obfuscation design based on the incomprehensibility of artificial neural networks
  to fight against reverse engineering tools including concolic testing. By training neural networks to simulate conditional behaviors of a program, we
  manage to precisely replace essential points of a program's control flow with neural network computations. Evaluations show that since the complexity
  of extracting rules from trained neural networks easily goes beyond the capability of program analysis tools, it is infeasible to apply concolic testing
  on code obfuscated with our method. Our method also incorporates only basic integer operations and simple loops, thus can be hard to be distinguished
  from regular programs.
added: 2021-02-25
address: Cham
authors:
- Haoyu Ma
- Xinjie Ma
- Weijie Liu
- Zhipeng Huang
- Debin Gao
- Chunfu Jia
booktitle: International Conference on Security and Privacy in Communication Networks
editor: Tian, Jing and Jing, Jiwu and Srivatsa, Mudhakar
isbn: 978-3-319-23829-6
layout: paper
pages: 287-304
publisher: Springer International Publishing
read: false
readings: []
title: Control Flow Obfuscation Using Neural Network to Fight Concolic Testing
year: 2015
notes:
papers:
---
{% include links.html %}
