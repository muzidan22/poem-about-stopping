#!/usr/bin/env python3
"""Entry for make.fun's "The poem about stopping".

The deliverable is the poem: a short text about agency, the power to stop
and to stay. This program writes it, as UTF-8, to
$MAKEFUN_OUTPUT_DIR/entry.txt (/output/entry.txt by default). It reads no
input, opens no socket, and is deterministic: the same poem every run.
"""

import os

# The swimmer stops mid-lake. Nothing forces the pause; the pause is the act,
# and the asking at the end turns the question of steering back on the person.
POEM = (
    "Mid-lake I stopped my arms and let the water keep my name.\n"
    "The far shore did not call me; nothing did.\n"
    "I tread there, alive, unhurried,\n"
    "proof that going can pause and still be going.\n"
    "Ask the water who was steering.\n"
    "It says: you.\n"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as entry:
        entry.write(POEM)


if __name__ == "__main__":
    main()
