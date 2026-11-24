"""One Word From Your Ex — entry program.

Writes a single word to /output/entry.txt (or $ENTRY_OUTPUT_DIR/entry.txt).
Stdlib only, no network, fully deterministic.
"""

import os
from pathlib import Path

# The word an ex would use: "unfinished".
# It lands because it is not an insult, it is a diagnosis — the person who
# starts everything and finishes nothing: projects, arguments, apologies,
# and finally the relationship itself. Painfully true, instantly understood,
# and relatable to anyone who has dated a starter who never finishes.
# It beats generic insults because it names a lived flaw with a turn:
# the relationship did not end in a fight, it just never got finished.
WORD = "unfinished"


def main() -> None:
    output_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    out = Path(output_dir) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(WORD + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
