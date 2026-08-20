#!/usr/bin/env python3
"""Create a verified portrait review map for Mango's irregular master sheet.

The portrait rows are not a 14-column grid. This map follows the 13 visible
portrait sprites in each row and uses the whitespace between them as crop
boundaries, so no portrait is cut by an artificial grid line.
"""

from __future__ import annotations

import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


SOURCE = Path("assets/characters/mango/shared/02_input/mango_master_reference_pixel_sheet_v1.png")
OUTPUT = Path(
    "assets/characters/mango/shared/02_input/"
    "mango_master_reference_pixel_sheet_v1_portrait_verified_clean_review.png"
)

# Actual visible portrait bounds, in reading order. The boxes deliberately
# include the whitespace between neighbours and exclude the battle row.
# Character silhouettes only, expanded by a small margin. Floating effects in
# the source sheet are intentionally excluded from the production input.
TOP = [
    (13, 14, 128, 136), (133, 14, 246, 136), (251, 15, 363, 136),
    (365, 12, 481, 136), (482, 13, 595, 136), (595, 15, 706, 136),
    (711, 13, 824, 136), (825, 8, 957, 136), (962, 16, 1075, 136),
    (1081, 15, 1192, 138), (1190, 12, 1311, 136), (1305, 16, 1417, 136),
    (1412, 15, 1526, 138),
]
BOTTOM = [
    (10, 146, 124, 272), (128, 144, 239, 272), (245, 144, 357, 272),
    (364, 145, 478, 272), (477, 146, 591, 273), (591, 147, 705, 273),
    (705, 145, 819, 272), (825, 146, 938, 272), (950, 146, 1062, 272),
    (1070, 147, 1180, 273), (1188, 147, 1299, 273), (1299, 148, 1414, 274),
    (1411, 147, 1525, 274),
]


def font() -> ImageFont.ImageFont:
    path = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
    return ImageFont.truetype(path, 24) if Path(path).exists() else ImageFont.load_default()


def main() -> int:
    with Image.open(SOURCE) as source:
        review = source.convert("RGBA")
        width, height = review.size

    boxes = TOP + BOTTOM
    draw = ImageDraw.Draw(review, "RGBA")
    cells = []
    fnt = font()
    for index, box in enumerate(boxes, 1):
        label = f"P{index:02d}"
        x0, y0, x1, y1 = box
        if not (0 <= x0 < x1 <= width and 0 <= y0 < y1 <= height):
            raise SystemExit(f"Invalid portrait bounds: {box}")
        text_box = draw.textbbox((0, 0), label, font=fnt)
        pad = 6
        label_box = (
            x0 + 3,
            y0 + 3,
            x0 + text_box[2] - text_box[0] + pad * 2,
            y0 + text_box[3] - text_box[1] + pad * 2,
        )
        draw.rounded_rectangle(label_box, radius=4, fill=(0, 0, 0, 210), outline=(255, 230, 80, 255), width=2)
        draw.text((label_box[0] + pad, label_box[1] + pad - 1), label, font=fnt, fill=(255, 240, 100, 255))
        cells.append({
            "label": label,
            "role": "portrait",
            "order": index,
            "box": list(box),
            "verified": True,
            "mapping_note": "13 visible portraits per row; silhouette crop with safety margin; effects excluded",
        })

    if OUTPUT.exists():
        raise SystemExit(f"Refusing to overwrite existing review copy: {OUTPUT}")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    review.save(OUTPUT)
    OUTPUT.with_suffix(OUTPUT.suffix + ".json").write_text(json.dumps({
        "source": str(SOURCE),
        "output": str(OUTPUT),
        "dimensions": [width, height],
        "mapping_basis": "explicit silhouette-bounded portrait crops with safety margin; not an equal grid",
        "portrait_count": len(cells),
        "invalid_legacy_ids": ["P27", "P28"],
        "cells": cells,
    }, indent=2) + "\n")
    print(f"Wrote {OUTPUT} and {OUTPUT}.json ({len(cells)} portraits)")


if __name__ == "__main__":
    raise SystemExit(main())
