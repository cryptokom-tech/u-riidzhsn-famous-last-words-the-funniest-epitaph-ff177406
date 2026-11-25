"""Famous Last Words: The Funniest Epitaph — one-line make.fun entry.

Writes the epitaph to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

LINE = "'It's perfectly safe,' I said. It was — for everyone standing behind me."

MAX_CHARS = 150


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE)
    with open(path, encoding="utf-8") as fh:
        written = fh.read()
    assert written == LINE, "entry.txt does not match the epitaph"
    assert 1 <= len(written) <= MAX_CHARS, "epitaph must be 1-150 characters"
    assert written.strip(), "epitaph must not be whitespace only"


if __name__ == "__main__":
    main()
