#!/usr/bin/env python3
"""The Self-Checkout Is Judging You — make.fun entry.

Writes one funny remark in the voice of a judgmental self-checkout machine
to /output/entry.txt. Gauntlet winner (3-0): the ready-meal line.
"""

# The entry line (92 chars, single line, UTF-8). Chosen by a 7-round local
# pairwise gauntlet over 30 candidates, judged on the sealed criteria order:
# machine voice first, real laugh on a single read, smug and petty about the
# basket, tight, fresh.
LINE = "One ready meal, one fork, no plate. Dinner for one, eaten standing up, over the sink. Again."


def main():
    """Write the entry line to /output/entry.txt."""
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
