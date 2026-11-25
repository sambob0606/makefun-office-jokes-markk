#!/usr/bin/env python3
"""One-Line Office Jokes (make.fun u-markk-st-one-line-office-jokes-a51f2bcc).

Writes exactly one single-line joke about office life to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Stdlib only; no input, no network.
"""

import os

JOKE = (
    "The printer only jams when the document is urgent, "
    "which is how I know it reads the subject line."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = JOKE.strip()
    assert 1 <= len(text) <= 199, f"entry must be 1-199 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
