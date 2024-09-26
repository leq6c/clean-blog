import os


def get_template_dir():
    return "builder/template"


def get_template_static_dir():
    return os.path.join(get_template_dir(), "static")


def get_asset_paths():
    return ["img", "css", "assets"]
