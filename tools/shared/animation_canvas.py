#!/usr/bin/env python3
"""Place an actual-size anchor into an opaque white animation grid."""

from __future__ import annotations

import argparse
from pathlib import Path

try:
    from PIL import Image
except ImportError as exc:  # pragma: no cover
    raise SystemExit("Install Pillow first: python3 -m pip install pillow") from exc


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("anchor", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--columns", type=int, required=True)
    parser.add_argument("--rows", type=int, default=1)
    parser.add_argument("--cell-width", type=int, required=True, help="Actual target frame width")
    parser.add_argument("--cell-height", type=int, required=True, help="Actual target frame height")
    parser.add_argument("--scale", type=int, default=1, help="Nearest-neighbour scale applied to the complete grid after placement")
    parser.add_argument("--anchor-column", type=int, default=0)
    parser.add_argument("--anchor-row", type=int, default=0)
    args = parser.parse_args()
    if args.columns < 1 or args.rows < 1:
        raise SystemExit("columns and rows must be positive")
    if not (0 <= args.anchor_column < args.columns and 0 <= args.anchor_row < args.rows):
        raise SystemExit("anchor cell is outside the canvas")

    anchor = Image.open(args.anchor).convert("RGBA")
    if anchor.width > args.cell_width or anchor.height > args.cell_height:
        raise SystemExit("Anchor is larger than its target frame cell; crop or fix the role contract first")
    if args.scale < 1:
        raise SystemExit("scale must be a positive integer")
    # OpenAI sprite generation uses an opaque pure-white background. Keep the
    # working canvas aligned with that contract instead of emitting alpha.
    canvas = Image.new("RGBA", (args.columns * args.cell_width, args.rows * args.cell_height), (255, 255, 255, 255))
    x = args.anchor_column * args.cell_width + (args.cell_width - anchor.width) // 2
    y = args.anchor_row * args.cell_height + (args.cell_height - anchor.height)
    canvas.alpha_composite(anchor, (x, y))
    if args.scale > 1:
        canvas = canvas.resize((canvas.width * args.scale, canvas.height * args.scale), Image.Resampling.NEAREST)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(args.output)
    print(f"Placed actual-size {args.anchor.size if hasattr(args.anchor, 'size') else anchor.size} anchor into cell {args.anchor_column},{args.anchor_row}; output={canvas.size[0]}x{canvas.size[1]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
