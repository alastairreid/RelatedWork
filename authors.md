---
title: Authors
layout: default
regenerate: true
---

<div class="posts">
    <ul>
{% for author in site.data.authors %}
        <li> {{author["name"]}}: {% for paper in author["papers"] %} {% assign name = paper | split: "/" %} <a href="{{site.baseurl}}/{{paper}}">{{ name[1] }}</a> {% endfor %}
        </li>
{% endfor %}
    </ul>
</div>
