import os

import mdtex2html
from render import load_template, render, render_metadata, render_one


def join_tags(tags):
    return ", ".join(tags)


def get_post_url(post):
    return os.path.splitext(post["content"])[0] + ".html"


def render_post(post, metadata, src_dir):
    html = load_template("post.html")
    html = render_metadata(html, metadata)

    filename = get_post_url(post)

    dic = post.copy()
    md = open(os.path.join(src_dir, post["content"]), "r", encoding="utf-8").read()
    dic["content"] = mdtex2html.convert(md)
    dic["tags"] = join_tags(post["tags"])

    return render(html, dic), filename


def render_post_list_item(template, post):
    dic = post.copy()
    dic["url"] = get_post_url(post)
    dic["tags"] = join_tags(post["tags"])
    return render(template, dic)
