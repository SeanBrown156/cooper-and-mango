#!/usr/bin/env python3
"""Tile candidate cells from a review map, with margin, for a fast visual bleed check.

Pixel-level heuristics (background-vs-content, seam continuity) do not
reliably distinguish "sprite fills its box" from "box cuts into a neighbour"
on this project's AI-generated, dithered/noisy pixel art — both look like
non-background content reaching the box edge. The only reliable check is a
human (or an agent) actually looking. This script makes that fast: each
selected cell is cropped with a margin beyond its own box, so a sprite that
spills into a neighbour is visibly still spilling in the preview, and a
cleanly bounded sprite shows a clear gap of neighbouring content around it.

Run this and inspect the output image before calling
extract_selected_sprite_cells.py; do not extract cells that have not been
looked at this way.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


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
    parser.add_argument("--master", type=Path, required=True)
    parser.add_argument("--review-map", type=Path, required=True)
    parser.add_argument("--select", required=True, help="Comma-separated IDs, e.g. P01,B03,O12")
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--margin", type=int, default=16, help="Pixels of neighbouring context shown around each box")
    parser.add_argument("--columns", type=int, default=4)
    parser.add_argument("--scale", type=int, default=3, help="Nearest-neighbour upscale factor for the preview")
    args = parser.parse_args()

    review = json.loads(args.review_map.read_text())
    selected = [item.strip().upper() for item in args.select.split(",") if item.strip()]
    cells = {str(item["label"]).upper(): item for item in review["cells"]}
    missing = sorted(set(selected) - cells.keys())
    if missing:
        raise SystemExit(f"Unknown cell IDs: {', '.join(missing)}")
    if not selected:
        raise SystemExit("Select at least one cell ID")

    with Image.open(args.master) as source:
        source.load()
        width, height = source.size
        tiles = []
        for label in selected:
            x0, y0, x1, y1 = cells[label]["box"]
            mx0, my0 = max(0, x0 - args.margin), max(0, y0 - args.margin)
            mx1, my1 = min(width, x1 + args.margin), min(height, y1 + args.margin)
            tile = source.crop((mx0, my0, mx1, my1)).convert("RGBA")
            tile = tile.resize((tile.width * args.scale, tile.height * args.scale), Image.NEAREST)
            draw = ImageDraw.Draw(tile, "RGBA")
            # Draw the actual box boundary (in scaled, margin-relative coords) so
            # it's obvious what's "inside the candidate" vs. "shown for context".
            box_local = (
                (x0 - mx0) * args.scale,
                (y0 - my0) * args.scale,
                (x1 - mx0) * args.scale,
                (y1 - my0) * args.scale,
            )
            draw.rectangle(box_local, outline=(255, 40, 40, 255), width=2)
            label_font = font_for(18)
            draw.rectangle((0, 0, 50, 22), fill=(0, 0, 0, 210))
            draw.text((4, 2), label, font=label_font, fill=(255, 240, 100, 255))
            tiles.append(tile)

    columns = min(args.columns, len(tiles))
    rows = (len(tiles) + columns - 1) // columns
    cell_w = max(t.width for t in tiles)
    cell_h = max(t.height for t in tiles)
    pad = 6
    sheet = Image.new("RGBA", (columns * (cell_w + pad) + pad, rows * (cell_h + pad) + pad), (60, 60, 60, 255))
    for index, tile in enumerate(tiles):
        row, column = divmod(index, columns)
        x = pad + column * (cell_w + pad)
        y = pad + row * (cell_h + pad)
        sheet.paste(tile, (x, y))

    args.out.parent.mkdir(parents=True, exist_ok=True)
    sheet.convert("RGB").save(args.out)
    print(f"Wrote {args.out} ({len(tiles)} cells, red outline = candidate box, margin = surrounding context)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
