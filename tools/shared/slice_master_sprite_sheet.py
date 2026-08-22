#!/usr/bin/env python3
"""Slice the role regions from a character-wide master sprite-sheet canvas."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image


ROLES = ("portrait", "battle", "overworld")


def box(value: str) -> tuple[int, int, int, int]:
    parts = value.split(",")
    if len(parts) != 4:
        raise argparse.ArgumentTypeError("box must be x0,y0,x1,y1")
    try:
        result = tuple(int(part) for part in parts)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("box coordinates must be integers") from exc
    x0, y0, x1, y1 = result
    if x0 < 0 or y0 < 0 or x1 <= x0 or y1 <= y0:
        raise argparse.ArgumentTypeError("box must have positive area and non-negative origin")
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--master", type=Path, required=True)
    parser.add_argument("--character", required=True)
    parser.add_argument("--variant", required=True, help="Master version, e.g. v2")
    parser.add_argument("--out-root", type=Path, required=True)
    parser.add_argument("--portrait-box", type=box, required=True)
    parser.add_argument("--battle-box", type=box, required=True)
    parser.add_argument("--overworld-box", type=box, required=True)
    args = parser.parse_args()

    with Image.open(args.master) as source:
        source.load()
        width, height = source.size
        boxes = {
            "portrait": args.portrait_box,
            "battle": args.battle_box,
            "overworld": args.overworld_box,
        }
        for role, coordinates in boxes.items():
            x0, y0, x1, y1 = coordinates
            if x1 > width or y1 > height:
                raise SystemExit(f"{role} box {coordinates} exceeds master size {width}x{height}")
            destination = args.out_root / role / "02_input"
            destination.mkdir(parents=True, exist_ok=True)
            output = destination / f"{args.character}_{role}_from_master_{args.variant}.png"
            if output.exists():
                raise SystemExit(f"Refusing to overwrite existing output: {output}")
            source.crop(coordinates).save(output)
            metadata = {
                "source_master": str(args.master),
                "character": args.character,
                "role": role,
                "variant": args.variant,
                "source_dimensions": [width, height],
                "crop_box": list(coordinates),
                "output": str(output),
                "status": "provisional_input_slice",
            }
            meta_dir = output.parent / "meta"
            meta_dir.mkdir(parents=True, exist_ok=True)
            (meta_dir / (output.name + ".json")).write_text(
                json.dumps(metadata, indent=2) + "\n"
            )
            print(f"Wrote {output}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
