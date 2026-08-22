#!/usr/bin/env python3
"""One-off migration: move existing <image>.png.json sidecars into meta/ subfolders.

Walks the given root(s) and, for every *.png.json file found next to its image,
moves it into a meta/ subfolder in the same directory (including inside any
superseded/<label>/ directory, so the pairing with its image is preserved).
Images and .import files are left untouched. Safe to re-run: already-migrated
files (already inside a meta/ dir) are skipped.
"""

from __future__ import annotations

import argparse
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("roots", nargs="+", type=Path, help="Directories to migrate")
    parser.add_argument("--dry-run", action="store_true", help="Print planned moves without moving")
    args = parser.parse_args()

    moved = 0
    for root in args.roots:
        for json_path in sorted(root.rglob("*.png.json")):
            if json_path.parent.name == "meta":
                continue
            meta_dir = json_path.parent / "meta"
            destination = meta_dir / json_path.name
            if destination.exists():
                raise SystemExit(f"Refusing to overwrite existing file: {destination}")
            print(f"{json_path} -> {destination}")
            if not args.dry_run:
                meta_dir.mkdir(parents=True, exist_ok=True)
                json_path.rename(destination)
            moved += 1

    print(f"{'Would move' if args.dry_run else 'Moved'} {moved} sidecar file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
