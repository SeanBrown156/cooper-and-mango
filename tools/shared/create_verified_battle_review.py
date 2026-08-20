#!/usr/bin/env python3
"""Create a manually verified review map for Mango's battle sprites.

The source sheet is an AI composition, not a regular grid. These bounds are
deliberately explicit and are kept separate from the numbered review copy.
"""

from __future__ import annotations

import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


SOURCE = Path("assets/characters/mango/shared/02_input/mango_master_reference_pixel_sheet_v1.png")
OUTPUT = Path("assets/characters/mango/shared/02_input/mango_master_reference_pixel_sheet_v1_battle_verified_review.png")

# Full visible battle sprites, in reading order. Padding preserves antialiasing
# and intentional shadows/effects without using the invalid equal-grid map.
SPRITES = [
    (24, 303, 104, 447), (154, 303, 251, 448), (277, 303, 392, 447),
    (426, 330, 539, 447), (567, 315, 687, 447), (733, 300, 937, 448),
    (965, 300, 1103, 447), (1127, 293, 1259, 453), (1307, 303, 1410, 455),
    (15, 456, 107, 603), (135, 469, 237, 603), (267, 469, 412, 603),
    (423, 472, 512, 603), (554, 465, 699, 603), (715, 473, 815, 606),
    (835, 485, 938, 596), (974, 472, 1089, 609), (1112, 457, 1245, 610),
    (1288, 463, 1382, 610), (1421, 464, 1520, 610),
    (153, 618, 215, 740), (286, 620, 375, 740), (438, 620, 547, 740),
    (583, 620, 683, 740), (713, 615, 826, 742), (866, 616, 927, 740),
]


def font() -> ImageFont.ImageFont:
    path = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
    return ImageFont.truetype(path, 24) if Path(path).exists() else ImageFont.load_default()


def main() -> int:
    with Image.open(SOURCE) as source:
        review = source.convert("RGBA")
        width, height = review.size

    draw = ImageDraw.Draw(review, "RGBA")
    selected = []
    fnt = font()
    for index, box in enumerate(SPRITES, 1):
        if not (0 <= box[0] < box[2] <= width and 0 <= box[1] < box[3] <= height):
            raise SystemExit(f"Invalid battle bounds: {box}")
        label = f"B{index:02d}"
        x0, y0, _, _ = box
        bbox = draw.textbbox((0, 0), label, font=fnt)
        pad = 6
        label_box = (x0 + 3, y0 + 3, x0 + bbox[2] - bbox[0] + pad * 2, y0 + bbox[3] - bbox[1] + pad * 2)
        draw.rounded_rectangle(label_box, radius=4, fill=(0, 0, 0, 210), outline=(255, 230, 80, 255), width=2)
        draw.text((label_box[0] + pad, label_box[1] + pad - 1), label, font=fnt, fill=(255, 240, 100, 255))
        selected.append({"label": label, "role": "battle", "order": index, "box": list(box), "verified": True})

    if OUTPUT.exists():
        raise SystemExit(f"Refusing to overwrite existing review copy: {OUTPUT}")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    review.save(OUTPUT)
    OUTPUT.with_suffix(OUTPUT.suffix + ".json").write_text(json.dumps({
        "source": str(SOURCE), "output": str(OUTPUT), "dimensions": [width, height],
        "mapping_basis": "explicit visible battle-sprite bounds; not an equal grid",
        "cells": selected,
    }, indent=2) + "\n")
    print(f"Wrote {OUTPUT} and {OUTPUT}.json")


if __name__ == "__main__":
    raise SystemExit(main())
