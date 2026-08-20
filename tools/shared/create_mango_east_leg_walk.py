#!/usr/bin/env python3
"""Create an explicit eight-frame east-facing Mango walk scaffold."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw


# Each tuple is (rear leg x, middle leg x, front leg x).  The alternating
# positions make the three visible side-view legs read as a walk rather than a
# vertical bob.  The source is 20x16, so the feet stay inside the original
# footprint throughout the cycle.
PHASES = (
    (3, 8, 13),
    (4, 9, 12),
    (4, 10, 13),
    (3, 9, 14),
    (3, 8, 13),
    (4, 9, 12),
    (4, 10, 13),
    (3, 9, 14),
)


def paint_leg(draw: ImageDraw.ImageDraw, x: int, y: int, outline: tuple[int, ...], fur: tuple[int, ...], shadow: tuple[int, ...]) -> None:
    """Paint a two-pixel-wide, one-pixel-foot side-view leg."""

    draw.point((x, y), fill=outline)
    draw.point((x + 1, y), fill=fur)
    draw.point((x, y + 1), fill=outline)
    draw.point((x + 1, y + 1), fill=fur)
    draw.point((x, y + 2), fill=outline)
    draw.point((x + 1, y + 2), fill=shadow)
    draw.point((x, y + 3), fill=outline)
    draw.point((x + 1, y + 3), fill=outline)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    source = Image.open(args.input).convert("RGBA")
    if source.size != (20, 16):
        raise SystemExit(f"expected 20x16 east frame, got {source.size}")

    transparent = (0, 0, 0, 0)
    outline = source.getpixel((3, 13))
    fur = source.getpixel((4, 13))
    shadow = source.getpixel((5, 13))
    args.output.mkdir(parents=True, exist_ok=True)

    for index, positions in enumerate(PHASES, start=1):
        frame = source.copy()
        draw = ImageDraw.Draw(frame)

        # The lower four rows contain the source feet and their cleanup area.
        # Leave the body edge at y=11 untouched.
        draw.rectangle((2, 12, 15, 15), fill=transparent)
        for x in positions:
            paint_leg(draw, x, 12, outline, fur, shadow)

        frame.save(args.output / f"mango-overworld-east-walk-frame-{index}.png")

    print(f"Generated {len(PHASES)} explicit-leg frames at {source.width}x{source.height}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
