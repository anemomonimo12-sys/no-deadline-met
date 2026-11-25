"""One Line, No Deadline Met — make.fun entry.

Writes a single-line joke giving an excuse for a missed deadline
to /output/entry.txt.
"""

import os

# The joke's turn: procrastination escalates until "tomorrow" itself
# takes legal action — the excuse becomes the punchline.
LINE = "I missed the deadline because I kept pushing it to tomorrow until tomorrow filed a restraining order."


def validate(line: str) -> None:
    """Check the line against the sealed gate: UTF-8 text, 1-200 chars,
    single line, not only whitespace."""
    if not line or not line.strip():
        raise ValueError("line is empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if len(line) > 200:
        raise ValueError(f"line is {len(line)} chars, over the 200-char cap")
    line.encode("utf-8")  # raises if not valid UTF-8


def main() -> None:
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
