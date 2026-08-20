#!/usr/bin/env python3
"""Extract only user-selected cells from a numbered sprite-sheet review map."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--master", type=Path, required=True)
    parser.add_argument("--review-map", type=Path, required=True)
    parser.add_argument("--select", required=True, help="Comma-separated IDs, e.g. P01,B03,O12")
    parser.add_argument("--out-root", type=Path, required=True)
    parser.add_argument("--character", required=True)
    parser.add_argument("--variant", required=True)
    args = parser.parse_args()

    review = json.loads(args.review_map.read_text())
    selected = {item.strip().upper() for item in args.select.split(",") if item.strip()}
    cells = {str(item["label"]).upper(): item for item in review["cells"]}
    missing = sorted(selected - cells.keys())
    if missing:
        raise SystemExit(f"Unknown cell IDs: {', '.join(missing)}")
    if not selected:
        raise SystemExit("Select at least one cell ID")

    with Image.open(args.master) as source:
        source.load()
        for label in sorted(selected):
            item = cells[label]
            x0, y0, x1, y1 = item["box"]
            role = str(item["role"])
            output_dir = args.out_root / role / "02_input"
            output_dir.mkdir(parents=True, exist_ok=True)
            output = output_dir / f"{args.character}_{role}_{label}_from_master_{args.variant}.png"
            if output.exists():
                raise SystemExit(f"Refusing to overwrite existing output: {output}")
            source.crop((x0, y0, x1, y1)).save(output)
            metadata = {
                "source_master": str(args.master),
                "review_map": str(args.review_map),
                "character": args.character,
                "role": role,
                "cell_id": label,
                "variant": args.variant,
                "crop_box": item["box"],
                "output": str(output),
                "status": "selected_provisional_input",
            }
            output.with_suffix(output.suffix + ".json").write_text(json.dumps(metadata, indent=2) + "\n")
            print(f"Wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
