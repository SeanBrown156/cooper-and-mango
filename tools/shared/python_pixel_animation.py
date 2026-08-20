#!/usr/bin/env python3
"""Create simple integer-pixel loops from a canonical PNG."""

from __future__ import annotations

import argparse
from pathlib import Path

try:
    from PIL import Image
except ImportError as exc:  # pragma: no cover
    raise SystemExit("Install Pillow first: python3 -m pip install pillow") from exc


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--mode", choices=("breathe", "bob", "sway"), default="breathe")
    parser.add_argument("--frames", type=int, default=4)
    args = parser.parse_args()
    if args.frames < 2:
        raise SystemExit("--frames must be at least 2")
    image = Image.open(args.input).convert("RGBA")
    args.output.mkdir(parents=True, exist_ok=True)
    offsets = [0, -1, 0, 1] if args.mode in ("breathe", "bob") else [0, -1, 0, 1]
    for index in range(args.frames):
        offset = offsets[index % len(offsets)]
        dx = offset if args.mode == "sway" else 0
        dy = offset if args.mode in ("breathe", "bob") else 0
        frame = Image.new("RGBA", image.size, (0, 0, 0, 0))
        frame.alpha_composite(image, (dx, dy))
        frame.save(args.output / f"frame_{index:03d}.png")
    print(f"Generated {args.frames} integer-pixel {args.mode} frames")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
