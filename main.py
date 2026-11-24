"""Write one original vending-machine pickup line to entry.txt.

Deterministic: the same line, byte for byte, on every run.
No randomness, no network, no clock, no input files.
"""

import os

LINE = "Forty snacks behind this glass and I'd still pick you \u2014 insert a coin, press B4, and I'll drop everything for you."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
