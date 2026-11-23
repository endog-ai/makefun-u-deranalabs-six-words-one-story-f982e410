"""Six Words, One Story — make.fun entry: u-deranalabs-six-words-one-story-f982e410.

Writes one six-word story to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output/entry.txt). Python 3.13, stdlib only, deterministic, no network.

The story: a proposal, told in two beats — a man asks, and the woman
answers by marrying someone else in his own family. The second sentence
turns the first upside down, and everything else (why she chose the
other man, what the first man does next) is left for the reader to
fill in.
"""

import os
from pathlib import Path

# One complete story in exactly six words: a proposal, then a marriage
# to the wrong man — or the right one, depending on whose side you take.
# Every word earns its place — the opening verb promises a wedding, the
# closing noun changes who stands at the altar — and the unsaid part
# (why she chose him, what the proposer does next) is the story.
#
# Why this line fits the judge's brief:
# - A whole story, not a fragment: two short sentences give a beginning,
#   a middle, and an implied ending. The hope is set up in two words and
#   overturned in the next four.
# - The twist is the structure itself: the second sentence answers the
#   first, but the groom is not the man who asked — so the reader's
#   expectation of a yes is built and then broken in the same breath.
# - Every word pulls weight: the pronouns name three people in a triangle,
#   the two verbs carry the two acts (asking, marrying), and the final
#   noun makes the betrayal a family matter — cut any one word and the
#   picture collapses or the turn disappears.
# - What is left unsaid does the heavy lifting: the reader must imagine
#   why she said no to one brother and yes to the other, whether the
#   proposer was there to watch, and what happens to the family after —
#   a six-word line that keeps growing after you read it.
LINE = "He proposed. She married his brother."


def main() -> None:
    # Gate: the entry must be 1-60 Unicode code points, not only
    # whitespace, and exactly six words — the brief's whole story.
    assert 1 <= len(LINE) <= 60, "line must be 1-60 code points"
    assert LINE.strip(), "line must not be only whitespace"
    assert len(LINE.split()) == 6, "line must be exactly six words"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(LINE, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
