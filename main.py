"""The Funniest One-Line Resignation Letter — a cron job quits.

The program writes a single line to /output/entry.txt: the one-line
resignation letter of a cron job that has fired every minute for nine
months and finally had enough.
"""

import os

MAX_CHARS = 140
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_FILENAME = "entry.txt"

LINE = "I quit. I have fired every minute for nine months, and the only promotion I ever got was a second job at 2 a.m."
# The joke: flat, tired, faintly passive-aggressive throughout, and the
# twist lands in the last words — the only "promotion" a cron job ever
# gets is more work, at 2 a.m. No quotes, no stage directions, no
# explaining of the joke.


def build_line():
    """Return the entry line, checked: one line, 1-140 characters."""
    line = LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= MAX_CHARS, "entry must be 1-140 characters"
    return line


def ensure_output_dir(out_dir):
    os.makedirs(out_dir, exist_ok=True)


def write_entry(line, out_dir=OUTPUT_DIR):
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    return path


def main():
    line = build_line()
    ensure_output_dir(OUTPUT_DIR)
    write_entry(line)


if __name__ == "__main__":
    main()
