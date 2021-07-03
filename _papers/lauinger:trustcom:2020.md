---
ENTRYTYPE: inproceedings
abstract: The Go programming language aims to provide memory and thread safety through measures such as automated memory management with garbage collection
  and a strict type system. However, it also offers a way of circumventing this safety net through the use of the unsafe package. While there are legitimate
  use cases for unsafe, developers must exercise caution to avoid introducing vulnerabilities like buffer overflows or memory corruption in general. In
  this work, we present go-geiger, a novel tool for Go developers to quantify unsafe usages in a project's source code and all of its dependencies. Using
  go-geiger, we conducted a study on the usage of unsafe in the top 500 most popular open-source Go projects on GitHub, including a manual analysis of 1,400
  code samples on how unsafe is used. From the projects using Go's module system, 38\% directly contain at least one unsafe usage, and 91\% contain at least
  one unsafe usage in the project itself or one of its transitive dependencies. Based on the usage patterns found, we present possible exploit vectors in
  different scenarios. Finally, we present go-safer, a novel static analysis tool to identify dangerous and common usage patterns that were previously undetected
  with existing tools.
added: 2021-06-28
authors:
- Johannes Lauinger
- Lars Baumgärtner
- Anna-Katharina Wickert
- Mira Mezini
booktitle: 2020 IEEE 19th International Conference on Trust, Security and Privacy in Computing and Communications (TrustCom)
doi: 10.1109/TrustCom50675.2020.00063
issn: 2324-9013
keywords: ''
layout: paper
month: Dec
number: ''
pages: 410-417
read: false
readings: []
title: 'Uncovering the hidden dangers: Finding unsafe Go code in the wild'
volume: ''
year: 2020
notes:
papers:
---
{% include links.html %}
