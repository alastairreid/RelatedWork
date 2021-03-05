---
layout: default
regenerate: true
---

[Unsummarized papers](#unsummarized) are at the end.

# Summarized papers

<div class="posts">
    <ul>
        {% assign papers = site.papers | where: "read",true | sort: "readings" | reverse %}
        {% for paper in papers %}
            <li>{{ paper.title }} [<a href="{{ site.baseurl }}{{ paper.url }}">{{ paper.slug }}</a>]</li>
        {% endfor %}
    </ul>
</div>

# Backlog of papers to summarize {#unsummarized}

<div class="posts">
    <ul>
        {% assign papers = site.papers | where: "read",false | sort: "added" | reverse %}
        {% for paper in papers %}
            <li>{{ paper.title }} [<a href="{{ site.baseurl }}{{ paper.url }}">{{ paper.slug }}</a>]</li>
        {% endfor %}
    </ul>
</div>


