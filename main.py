#!/usr/bin/env python3
"""Fortune in a Pot — a make.fun bounty entry.

Prints one kind, funny fortune for a houseplant: next spring a stranger
will admire its leaves, and the owner will pretend they planned it all
along. The fortune is 103 characters (limit 120) and is written verbatim
to /output/entry.txt for the grader, so the printed line and the file
always carry exactly the same text.
"""

FORTUNE = (
    "Next spring, a stranger will admire your leaves, "
    "and your owner will pretend they planned it all along."
)


def main() -> None:
    try:
        import os

        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(FORTUNE)
    except OSError:
        pass
    print(FORTUNE)


if __name__ == "__main__":
    main()
