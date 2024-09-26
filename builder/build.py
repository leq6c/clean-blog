import argparse
import os

from watcher import watch

from builder import build

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True)
    parser.add_argument("--output", type=str, required=True)
    parser.add_argument("--watch", action="store_true")
    args = parser.parse_args()

    if args.watch:
        dir = os.path.dirname(args.input)
        watch(dir, lambda: build(args.input, args.output))
    else:
        build(args.input, args.output)
