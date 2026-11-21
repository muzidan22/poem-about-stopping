#!/usr/bin/env python3
"""Entry for make.fun's "The poem about stopping".

The deliverable is the poem: a short text about agency, the power to stop
and to stay. This program writes it, as UTF-8, to
$MAKEFUN_OUTPUT_DIR/entry.txt (/output/entry.txt by default). It reads no
input, opens no socket, and is deterministic: the same poem every run.
"""

import os

# Climbing: the anchor's power is the power to stay, and holding is a choice
# as deliberate as letting go. The sky's stillness mirrors the held body.
POEM = (
    "My partner was falling and I was the anchor.\n"
    "I could have let go; that was the point.\n"
    "I held. The rope sang. The rock held.\n"
    "Above me the sky stayed exactly\n"
    "where it was, doing nothing\n"
    "like me, and on purpose.\n"
    "I have never done anything\n"
    "so much like choosing.\n"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as entry:
        entry.write(POEM)


if __name__ == "__main__":
    main()
