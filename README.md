# Clean blog

This is a clean blog builder written in Python. 

## Features

- Clean design
- No javascript
- Fast build

## How to write content

### Metadata

Metadata can be written in yaml format. Look at [example_src/blog.yaml](example_src/blog.yaml) for more details.

### Posts

Posts can be written in markdown format like [example_src/posts/some-nice-post.md](example_src/posts/some-nice-post.md).

## Usage

### Build

```bash
py builder/build.py --input example_src/blog.yaml --output dist
```

### Watch

```bash
py builder/build.py --input example_src/blog.yaml --output dist --watch
```

## License

MIT
