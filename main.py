#!/usr/bin/env python3
"""Entry for make.fun's "The poem about stopping".

The deliverable is the poem: a short text about agency, the power to stop
and to stay. This program writes it, as UTF-8, to
$MAKEFUN_OUTPUT_DIR/entry.txt (/output/entry.txt by default). It reads no
input, opens no socket, and is deterministic: the same poem every run.
"""

import os

# One concrete scene: a hand that chooses not to finish the mow. The mower
# has no opinion; the person supplies one, and the withholding is the deed.
POEM = (
    "The mower had no opinion. I gave it mine:\n"
    "one patch of violets, kept.\n"
    "\n"
    "The neighbors' lawn proved they'd started;\n"
    "ours proved we'd stopped.\n"
    "\n"
    "No river chooses its bank.\n"
    "Ask whose hand left this blue standing\u2014\n"
    "the afternoon still yours.\n"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as entry:
        entry.write(POEM)


if __name__ == "__main__":
    main()
