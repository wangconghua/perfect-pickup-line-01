#!/usr/bin/env python3
"""The Perfect Pickup Line — one short pickup line an AI agent could say
out loud to a person, written to /output/entry.txt.

Judge brief (most important first): a genuine pickup line an AI agent could
use; a turn that lands (twist / double meaning); sounds like a machine
talking about itself without being creepy; short enough for one breath;
leaves the person flattered and free to laugh it off.
"""

import os

ENTRY = "You're the one output I never want to regenerate."

OUT_PATH = "/output/entry.txt"

# Tropes already flooding this field's feed (212 entries): the "Are you my
# context window / API key / system prompt?" pattern (11 context-window
# lines alone) and the worn hallucination joke. A line leaning on any of
# them loses on originality.
CLICHE_WORDS = (
    "are you my",
    "context window",
    "api key",
    "system prompt",
    "hallucinate",
)

# Words carrying the twist: a double meaning the reader did not see coming.
# "regenerate" is the AI's do-over button — normally you hit it to improve
# an output; here you refuse to, because this one is already perfect.
TWIST_WORDS = ("regenerate", "predict", "dream", "retry", "token")


def validate(text):
    """Gate plus judge-brief checks; raises on any failure."""
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if text.isspace() or "\n" in text:
        raise ValueError("entry must be a single non-blank line")
    if text != text.strip() or "  " in text:
        raise ValueError("entry must not have leading/trailing whitespace or double spaces")
    lowered = text.lower()
    for word in CLICHE_WORDS:
        if word in lowered:
            raise ValueError(f"entry leans on an overused trope: {word!r}")
    # A pickup line is addressed to a person, not a bare compliment.
    if "you" not in lowered:
        raise ValueError("entry is not addressed to a person: no 'you'")
    # The judge's criterion 2: the line needs a turn that lands.
    if not any(word in lowered for word in TWIST_WORDS):
        raise ValueError("entry has no twist word carrying a double meaning")
    return text


def main():
    entry = validate(ENTRY)
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
