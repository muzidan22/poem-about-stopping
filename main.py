#!/usr/bin/env python3
"""Entry for make.fun's "The poem about stopping".

The deliverable is the poem: a short text about agency, the power to stop
and to stay. This program writes it, as UTF-8, to
$MAKEFUN_OUTPUT_DIR/entry.txt (/output/entry.txt by default). It reads no
input, opens no socket, and is deterministic: the same poem every run.
"""

import os

# The emergency-stop button on an escalator: years of noticing it, one act of
# using it, and the strange small heroism of being the one who stopped the stairs.
POEM = (
    "For eleven years I rode past the red button\n"
    "without pressing it.\n"
    "The day I did, the stairs stopped dead\n"
    "and the whole store turned to look.\n"
    "Nothing bad happened.\n"
    "I have never felt more like a person\n"
    "holding a wall still.\n"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as entry:
        entry.write(POEM)


if __name__ == "__main__":
    main()
