import os

from render import load_template, render, render_metadata, render_one
from render_post import render_post_list_item


def render_hidden(html, target):
    html = render_one(html, f"{target}-class", "hidden")
    return render_one(html, target, "")


def render_visible(html, target):
    return render_one(html, f"{target}-class", "visible")


def render_works(html, works):
    template = load_template("parts/index/list-item-work.html")

    if len(works) == 0:
        return render_hidden(html, "works")

    html = render_visible(html, "works")

    works_html = ""
    for work in works:
        works_html += render(template, work)

    return render_one(html, "works", works_html)


def render_posts(html, posts):
    template = load_template("parts/index/list-item-post.html")

    if len(posts) == 0:
        return render_hidden(html, "posts")

    html = render_visible(html, "posts")

    posts_html = ""
    for post in posts:
        posts_html += render_post_list_item(template, post)

    return render_one(html, "posts", posts_html)


def render_design(html, design):
    template = load_template("parts/index/list-item-design.html")

    if len(design) == 0:
        return render_hidden(html, "design")

    html = render_visible(html, "design")

    design_html = ""
    key = "a"
    for design in design:
        dic = design.copy()
        dic["id"] = key
        design_html += render(template, dic)
        key = chr(ord(key) + 1)

    return render_one(html, "design", design_html)


def render_index(metadata, works, design, posts):
    html = load_template("index.html")
    html = render_metadata(html, metadata)
    html = render_works(html, works)
    html = render_posts(html, posts)
    html = render_design(html, design)
    return html, "index.html"
