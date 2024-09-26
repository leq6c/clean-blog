import os

from constant import get_template_dir


def load_template(file_path):
    return open(
        os.path.join(get_template_dir(), file_path), "r", encoding="utf-8"
    ).read()


def render(html, data, prefix=""):
    if prefix != "":
        prefix = prefix + "."
    for key, value in data.items():
        html = html.replace("{{" + prefix + key + "}}", value)
    return html


def render_one(html, key, value):
    return render(html, {key: value})


def render_metadata(html, metadata):
    return render(html, metadata, "metadata")
