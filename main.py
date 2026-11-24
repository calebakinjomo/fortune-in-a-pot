#!/usr/bin/env python3
"""Fortune in a Pot — a make.fun bounty entry.

Prints one kind, funny fortune for a houseplant (103 characters),
and writes the same line to /output/entry.txt for the grader.
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
