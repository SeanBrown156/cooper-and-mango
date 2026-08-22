#!/usr/bin/env python3
"""Validate image dimensions, alpha hygiene, and optional palette membership."""

from __future__ import annotations

import argparse
from pathlib import Path

try:
    from PIL import Image
except ImportError as exc:  # pragma: no cover
    raise SystemExit("Install Pillow first: python3 -m pip install pillow") from exc


def read_palette(path: Path) -> set[tuple[int, int, int]]:
    colors = set()
    for line in path.read_text().splitlines():
        value = line.strip().lstrip("#")
        if len(value) == 6:
            colors.add(tuple(int(value[index:index + 2], 16) for index in (0, 2, 4)))
    return colors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("image", type=Path)
    parser.add_argument("--width", type=int)
    parser.add_argument("--height", type=int)
    parser.add_argument("--palette", type=Path)
    parser.add_argument("--require-alpha", action="store_true")
    args = parser.parse_args()
    image = Image.open(args.image).convert("RGBA")
    failures = []
    if args.width is not None and image.width != args.width:
        failures.append(f"width {image.width} != {args.width}")
    if args.height is not None and image.height != args.height:
        failures.append(f"height {image.height} != {args.height}")
    if args.require_alpha and image.getchannel("A").getbbox() is None:
        failures.append("image has no visible pixels")
    if args.palette:
        palette = read_palette(args.palette)
        pixels = set(image.getdata())
        rgb_pixels = {pixel[:3] for pixel in pixels if pixel[3]}
        unexpected = sorted(rgb_pixels - palette)
        if unexpected:
            failures.append(f"{len(unexpected)} visible RGB colours outside palette")
    if failures:
        print(f"INVALID {args.image}")
        for failure in failures:
            print(f"  - {failure}")
        return 2
    print(f"VALID {args.image}: {image.width}x{image.height}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
