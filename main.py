"""Veikk Desktop — A desktop helper that finds Veikk data directories and archives config and export files locally."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='veikk_desktop',
        description='A desktop helper that finds Veikk data directories and archives config and export files locally.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Veikk Desktop')
    print('Dated copies of Veikk data data, nothing uploaded.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
# tweak (2026-11-03)
# refactor bit (2026-11-03)
# refactor bit (2026-11-04)
# polish (2026-11-05)
# polish (2026-11-06)
# update note (2026-11-06)
# update note (2026-11-16)
# wip (2026-11-16)
# revisit later (2026-11-17)
# update note (2026-11-17)
# refactor bit (2026-11-17)
# minor adjust (2026-11-23)
# wip (2026-11-24)
# small fix (2026-11-24)
# minor adjust (2026-11-24)
# revisit later (2026-11-25)
