#!/usr/bin/env python3
"""Prepare a crisp enlarged, white-backed reference for a Sora motion test."""

from __future__ import annotations

from collections import deque
from pathlib import Path

from PIL import Image


def main() -> int:
    source = Image.open(Path("assets/characters/mango/overworld/03_wip/south/animation/pixellab/frame_0.png")).convert("RGBA")
    pixels = source.load()
    background = pixels[0, 0]
    queue = deque((x, y) for x in range(source.width) for y in (0, source.height - 1))
    queue.extend((x, y) for y in range(source.height) for x in (0, source.width - 1))
    seen: set[tuple[int, int]] = set()
    while queue:
        x, y = queue.popleft()
        if (x, y) in seen or not (0 <= x < source.width and 0 <= y < source.height):
            continue
        seen.add((x, y))
        if pixels[x, y] != background:
            continue
        pixels[x, y] = (255, 255, 255, 0)
        queue.extend(((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)))

    sprite = source.resize((256, 320), Image.Resampling.NEAREST)
    canvas = Image.new("RGBA", (1280, 720), (255, 255, 255, 255))
    canvas.alpha_composite(sprite, ((canvas.width - sprite.width) // 2, (canvas.height - sprite.height) // 2))
    canvas.convert("RGB").save(Path("assets/characters/mango/overworld/03_wip/south/animation/sora/mango_south_reference_1280x720.png"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
