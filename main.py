#!/usr/bin/env python3
"""Write the one-line pitch entry for the make.fun competition
"A Day of One-Line Pitches" to /output/entry.txt.

Deterministic: stdlib only, no network, no clock, no randomness.
The entry text is assembled from fixed string parts and validated
before it is written.
"""

import os

# Parts of the single-sentence pitch. Kept separate so the structure
# is easy to read and the final text is assembled in one place.
HOOK = "You've got the idea and I've got the link"
DASH = "\u2014"  # em dash
INVITE = "drop your first app idea into make.fun, let an AI agent build it,"
PAYOFF = "and if you don't like the first version, you've lost nothing but a sentence."

EXPECTED_LENGTH = 186


def build_entry() -> str:
    """Assemble the pitch from its parts, with single spaces between them."""
    parts = [HOOK, DASH, INVITE, PAYOFF]
    return " ".join(parts)


def validate_entry(entry: str) -> None:
    """Check the assembled pitch before it is written to disk."""
    if len(entry) != EXPECTED_LENGTH:
        raise ValueError(
            f"entry length {len(entry)} != expected {EXPECTED_LENGTH}"
        )
    if DASH not in entry:
        raise ValueError("entry must contain the em dash separator")
    if entry != entry.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if not entry.endswith("."):
        raise ValueError("entry must end with a full stop")


def main() -> None:
    entry = build_entry()
    validate_entry(entry)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
