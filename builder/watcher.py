import time

from constant import get_template_dir
from watchfiles import watch as _watch


def watch(target_dir, fn):
    fn()
    print("watching")
    for changes in _watch(target_dir, get_template_dir()):
        for action, path in changes:
            print("rebuilding...")
            start = time.time()
            fn()
            print(f"rebuild complete ({time.time() - start:.2f}s)")
