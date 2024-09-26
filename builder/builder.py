import os
import shutil

import yaml
from constant import get_asset_paths, get_template_static_dir
from render_index import render_index
from render_post import render_post


def load_yaml(file_path):
    with open(file_path, "r") as file:
        return yaml.safe_load(file)


def get_or_empty(data, key):
    if key in data:
        return data[key]
    return []


def build(input_path, output_path):
    data = load_yaml(input_path)

    metadata = data["metadata"]
    works = get_or_empty(data, "works")
    design = get_or_empty(data, "design")
    posts = get_or_empty(data, "posts")

    os.makedirs(output_path, exist_ok=True)

    # copy static files
    shutil.copytree(get_template_static_dir(), output_path, dirs_exist_ok=True)

    # copy assets
    input_dir = os.path.dirname(input_path)
    for target in get_asset_paths():
        if not os.path.exists(os.path.join(input_dir, target)):
            continue
        shutil.copytree(
            os.path.join(input_dir, target),
            os.path.join(output_path, target),
            dirs_exist_ok=True,
        )

    # render index
    index_html, index_filename = render_index(metadata, works, design, posts)
    with open(os.path.join(output_path, index_filename), "w", encoding="utf-8") as file:
        file.write(index_html)

    # render posts
    for post in posts:
        post_html, post_filename = render_post(post, metadata, input_dir)
        target_filepath = os.path.join(output_path, post_filename)
        os.makedirs(os.path.dirname(target_filepath), exist_ok=True)
        with open(target_filepath, "w", encoding="utf-8") as file:
            file.write(post_html)
