---
title: Authors
layout: default
regenerate: true
---

{% for author in site.data.authors %}
- {{author["name"]}}: {% for paper in author["papers"] %} {% assign name = paper | split: "/" %} [{{ name[1] }}](/{{paper}}) {% endfor %}
{% endfor %}
