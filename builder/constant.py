import os


def get_template_dir():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(dir_path, "template")


def get_template_static_dir():
    return os.path.join(get_template_dir(), "static")


def get_asset_paths():
    return ["img", "css", "assets"]
