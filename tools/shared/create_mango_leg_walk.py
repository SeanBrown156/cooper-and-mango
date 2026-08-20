#!/usr/bin/env python3
"""Create a deliberate tiny south-facing walk by moving the visible legs."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw


PHASES = (
    ((3, 15, 5, 17), (10, 16, 12, 18)),
    ((4, 16, 6, 18), (9, 15, 11, 17)),
    ((3, 16, 5, 18), (10, 15, 12, 17)),
    ((4, 15, 6, 17), (9, 16, 11, 18)),
    ((3, 15, 5, 17), (10, 16, 12, 18)),
    ((4, 16, 6, 18), (9, 15, 11, 17)),
    ((3, 16, 5, 18), (10, 15, 12, 17)),
    ((4, 15, 6, 17), (9, 16, 11, 18)),
)


def paint_leg(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], dark: tuple[int, ...], fur: tuple[int, ...]) -> None:
    x0, y0, x1, y1 = box
    draw.rectangle(box, fill=dark)
    if x1 - x0 >= 2:
        draw.rectangle((x0 + 1, y0, x1 - 1, y1 - 1), fill=fur)
    draw.point((x0 + 1, y1), fill=dark)
    draw.point((x1 - 1, y1), fill=dark)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    source = Image.open(args.input).convert("RGBA")
    if source.size != (16, 20):
        raise SystemExit(f"expected 16x20 south frame, got {source.size}")

    background = source.getpixel((0, 0))
    shadow = source.getpixel((3, 16))
    fur = source.getpixel((4, 16))
    args.output.mkdir(parents=True, exist_ok=True)

    for index, (left, right) in enumerate(PHASES):
        frame = source.copy()
        draw = ImageDraw.Draw(frame)
        draw.rectangle((3, 15, 6, 18), fill=background)
        draw.rectangle((9, 15, 12, 18), fill=background)
        paint_leg(draw, left, shadow, fur)
        paint_leg(draw, right, shadow, fur)
        frame.save(args.output / f"frame_{index}.png")

    print(f"Generated {len(PHASES)} explicit-leg frames at {source.width}x{source.height}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
