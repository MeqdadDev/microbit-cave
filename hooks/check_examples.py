"""MkDocs hook: warn (and fail `mkdocs build --strict`) when an example page's front matter is incomplete."""
import logging
from pathlib import Path

log = logging.getLogger("mkdocs.hooks.check_examples")

EXAMPLE_DIRS = ("microbit/", "tools/")
REQUIRED = ("title", "description", "tags", "level", "board", "parts", "source")
LEVELS = ("Beginner", "Intermediate", "Advanced")


def on_page_markdown(markdown, page, config, files):
    src = page.file.src_uri
    if not src.startswith(EXAMPLE_DIRS) or src.endswith("index.md"):
        return markdown

    meta = page.meta
    missing = [key for key in REQUIRED if not meta.get(key)]
    if missing:
        # An unquoted ": " in the front matter leaves page.meta empty, so it lands here too.
        log.warning("%s: missing %s in front matter (quote values containing ': ')", src, ", ".join(missing))
        return markdown

    if meta["level"] not in LEVELS:
        log.warning("%s: level must be one of %s", src, ", ".join(LEVELS))
    elif meta["level"] not in meta["tags"]:
        log.warning("%s: add the level '%s' to tags", src, meta["level"])

    root = Path(config.config_file_path).parent
    for path in meta["source"] + (meta.get("libraries") or []):
        if not (root / path).is_file():
            log.warning("%s: source file not found: %s", src, path)
    return markdown
