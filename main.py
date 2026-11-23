#!/usr/bin/env python3
"""Write the one-line pitch entry for the make.fun competition
"A Day of One-Line Pitches" to /output/entry.txt.

Deterministic: stdlib only, no network, no clock, no randomness.
The entry text is a single fixed string literal.
"""

import os

ENTRY = (
    "You've got the idea and I've got the link \u2014 drop your first app idea "
    "into make.fun, let an AI agent build it, and if you don't like the first "
    "version, you've lost nothing but a sentence."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
