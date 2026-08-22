#!/usr/bin/env python3
"""Create a numbered review copy of a sprite sheet without changing the source."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def parse_region(value: str) -> tuple[str, tuple[int, int, int, int], int, int]:
    try:
        name, coordinates, columns, rows = value.split(":")
        box = tuple(int(part) for part in coordinates.split(","))
        columns = int(columns)
        rows = int(rows)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(
            "region must be name:x0,y0,x1,y1:columns:rows"
        ) from exc
    if len(box) != 4 or columns < 1 or rows < 1:
        raise argparse.ArgumentTypeError("invalid region box or grid")
    x0, y0, x1, y1 = box
    if x0 < 0 or y0 < 0 or x1 <= x0 or y1 <= y0:
        raise argparse.ArgumentTypeError("region box must have positive area")
    return name, box, columns, rows


def font_for(size: int) -> ImageFont.ImageFont:
    candidates = (
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/System/Library/Fonts/Supplemental/DejaVuSans-Bold.ttf",
    )
    for candidate in candidates:
        path = Path(candidate)
        if path.exists():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--region", action="append", type=parse_region, required=True)
    args = parser.parse_args()

    with Image.open(args.input) as source:
        source = source.convert("RGBA")
        width, height = source.size
        review = source.copy()
    draw = ImageDraw.Draw(review, "RGBA")
    mapping: list[dict[str, object]] = []

    for name, box, columns, rows in args.region:
        x0, y0, x1, y1 = box
        if x1 > width or y1 > height:
            raise SystemExit(f"{name} region exceeds image size {width}x{height}")
        cell_width = (x1 - x0) / columns
        cell_height = (y1 - y0) / rows
        prefix = "".join(word[:1].upper() for word in name.split("-") if word)
        label_size = max(16, min(30, int(min(cell_width, cell_height) * 0.16)))
        font = font_for(label_size)
        for row in range(rows):
            for column in range(columns):
                index = row * columns + column + 1
                left = int(round(x0 + column * cell_width))
                top = int(round(y0 + row * cell_height))
                right = int(round(x0 + (column + 1) * cell_width))
                bottom = int(round(y0 + (row + 1) * cell_height))
                label = f"{prefix}{index:02d}"
                bbox = draw.textbbox((0, 0), label, font=font)
                text_width = bbox[2] - bbox[0]
                text_height = bbox[3] - bbox[1]
                pad = max(4, label_size // 5)
                label_box = (left + 4, top + 4, left + text_width + pad * 2, top + text_height + pad * 2)
                draw.rounded_rectangle(label_box, radius=4, fill=(0, 0, 0, 205), outline=(255, 230, 80, 255), width=2)
                draw.text((label_box[0] + pad, label_box[1] + pad - 1), label, font=font, fill=(255, 240, 100, 255))
                mapping.append({"label": label, "role": name, "row": row + 1, "column": column + 1, "box": [left, top, right, bottom]})

    if args.out.exists():
        raise SystemExit(f"Refusing to overwrite existing review copy: {args.out}")
    args.out.parent.mkdir(parents=True, exist_ok=True)
    review.save(args.out)
    meta_dir = args.out.parent / "meta"
    meta_dir.mkdir(parents=True, exist_ok=True)
    meta_path = meta_dir / (args.out.name + ".json")
    meta_path.write_text(json.dumps({"source": str(args.input), "output": str(args.out), "dimensions": [width, height], "cells": mapping}, indent=2) + "\n")
    print(f"Wrote {args.out} and {meta_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
