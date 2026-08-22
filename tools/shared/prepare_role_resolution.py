#!/usr/bin/env python3
"""Prepare one selected sprite cell at the governed role resolution."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

from PIL import Image


TARGETS = {
    "overworld": (20, 16),
    "battle": (32, 32),
    "portrait": (40, 40),
}


def remove_edge_background(image: Image.Image, tolerance: int) -> Image.Image:
    """Remove an edge-connected near-uniform background without touching interiors."""
    pixels = image.load()
    width, height = image.size
    queue: list[tuple[int, int]] = []
    visited: set[tuple[int, int]] = set()
    seeds: list[tuple[int, int, tuple[int, int, int, int]]] = []
    for x in range(width):
        seeds.extend(((x, 0, pixels[x, 0]), (x, height - 1, pixels[x, height - 1])))
    for y in range(height):
        seeds.extend(((0, y, pixels[0, y]), (width - 1, y, pixels[width - 1, y])))
    background = min(seeds, key=lambda item: sum(item[2][:3]))[2]

    def close(color: tuple[int, int, int, int]) -> bool:
        distance = math.sqrt(sum((color[i] - background[i]) ** 2 for i in range(3)))
        return distance <= tolerance

    for x, y, color in seeds:
        if (x, y) not in visited and close(color):
            visited.add((x, y))
            queue.append((x, y))
    while queue:
        x, y = queue.pop()
        pixels[x, y] = (pixels[x, y][0], pixels[x, y][1], pixels[x, y][2], 0)
        for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if 0 <= nx < width and 0 <= ny < height and (nx, ny) not in visited:
                visited.add((nx, ny))
                if close(pixels[nx, ny]):
                    queue.append((nx, ny))
    return image


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--role", choices=sorted(TARGETS), required=True)
    parser.add_argument("--background-tolerance", type=int, default=36)
    parser.add_argument("--keep-background", action="store_true")
    args = parser.parse_args()

    target_width, target_height = TARGETS[args.role]
    with Image.open(args.input) as source:
        source = source.convert("RGBA")
        source_width, source_height = source.size
        background_removed = False
        if not args.keep_background:
            source = remove_edge_background(source, args.background_tolerance)
            background_removed = True
        scale = min(target_width / source_width, target_height / source_height)
        resized_size = (
            max(1, round(source_width * scale)),
            max(1, round(source_height * scale)),
        )
        resized = source.resize(resized_size, Image.Resampling.NEAREST)
        background = Image.new("RGBA", (target_width, target_height), (0, 0, 0, 0))
        left = (target_width - resized.width) // 2
        top = (target_height - resized.height) // 2
        background.alpha_composite(resized, (left, top))

    args.out.parent.mkdir(parents=True, exist_ok=True)
    if args.out.exists():
        raise SystemExit(f"Refusing to overwrite existing output: {args.out}")
    background.save(args.out)
    metadata = {
        "source": str(args.input),
        "output": str(args.out),
        "role": args.role,
        "target_dimensions": [target_width, target_height],
        "source_dimensions": [source_width, source_height],
        "resampling": "nearest-neighbour",
        "fit": "contain",
        "background_removal": "edge-connected flood fill" if background_removed else "kept",
        "background_tolerance": args.background_tolerance if background_removed else None,
        "status": "resolution_prepared_input",
        "review_required": "confirm landmarks and silhouette before PixelLab",
    }
    meta_dir = args.out.parent / "meta"
    meta_dir.mkdir(parents=True, exist_ok=True)
    meta_path = meta_dir / (args.out.name + ".json")
    meta_path.write_text(json.dumps(metadata, indent=2) + "\n")
    print(f"Wrote {args.out} and {meta_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
