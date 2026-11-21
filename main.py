#!/usr/bin/env python3
"""Entry for make.fun's "The poem about stopping".

The deliverable is the poem: a short text about agency, the power to stop
and to stay. This program writes it, as UTF-8, to
$MAKEFUN_OUTPUT_DIR/entry.txt (/output/entry.txt by default). It reads no
input, opens no socket, and is deterministic: the same poem every run.
"""

import os

# Learning to drive with a father: the gas is learned in a day, the brake in
# years. The last image is the choice to stay put, taken as the poem's own.
POEM = (
    "My father taught me the gas in a day.\n"
    "The brake took years\u2014\n"
    "a foot learning to hover,\n"
    "a hill trusting us back.\n"
    "He is gone. Tonight I park\n"
    "and sit in the dark driveway,\n"
    "the key still in, going nowhere\n"
    "on purpose.\n"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as entry:
        entry.write(POEM)


if __name__ == "__main__":
    main()
