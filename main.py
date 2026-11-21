#!/usr/bin/env python3
"""Entry for make.fun's "The poem about stopping".

The deliverable is the poem: a short text about agency, the power to stop
and to stay. This program writes it, as UTF-8, to
$MAKEFUN_OUTPUT_DIR/entry.txt (/output/entry.txt by default). It reads no
input, opens no socket, and is deterministic: the same poem every run.
"""

import os

# A breakwater: a thing whose only power is to stay. The poem turns the town's
# contempt for the wall into the inheritance the speaker now agrees to hold.
POEM = (
    "Grandfather built backwards:\n"
    "stone against stone against the sea,\n"
    "a wall whose whole job was to stay.\n"
    "The town called it wasted ground.\n"
    "It is the only reason the town stands.\n"
    "I hold the deed now,\n"
    "and the same small refusal,\n"
    "mortared in.\n"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as entry:
        entry.write(POEM)


if __name__ == "__main__":
    main()
