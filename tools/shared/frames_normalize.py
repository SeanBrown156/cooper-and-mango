#!/usr/bin/env python3
"""Normalize PNG frames while preserving explicit character landmarks."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

try:
    from PIL import Image, ImageChops
except ImportError as exc:  # pragma: no cover - dependency diagnostic
    raise SystemExit("Install Pillow first: python3 -m pip install pillow") from exc


def trim_bounds(image: Image.Image):
    alpha = image.getchannel("A") if image.mode == "RGBA" else image.convert("RGBA").getchannel("A")
    return alpha.getbbox()


def place_frame(
    source: Image.Image,
    size: tuple[int, int],
    baseline: int | None,
    landmarks: dict[str, float] | None,
    target_body_height: int | None,
    target_pivot_x: int | None,
) -> Image.Image:
    source = source.convert("RGBA")
    if landmarks and target_body_height:
        head_y = float(landmarks["head_y"])
        feet_y = float(landmarks["feet_y"])
        body_height = feet_y - head_y
        if body_height <= 0:
            raise ValueError("feet_y must be greater than head_y")
        scale = target_body_height / body_height
        source = source.resize((max(1, round(source.width * scale)), max(1, round(source.height * scale))), Image.Resampling.NEAREST)
        feet_x = float(landmarks.get("feet_x", source.width / 2 / scale)) * scale
        feet_y *= scale
    else:
        feet_x = source.width / 2
        feet_y = source.height
    bounds = trim_bounds(source)
    if not bounds:
        return Image.new("RGBA", size, (0, 0, 0, 0))
    cropped = source.crop(bounds)
    feet_x -= bounds[0]
    feet_y -= bounds[1]
    canvas = Image.new("RGBA", size, (0, 0, 0, 0))
    if landmarks and target_body_height:
        target_feet_y = baseline if baseline is not None else size[1] - 1
        source_x = target_pivot_x if target_pivot_x is not None else size[0] // 2
        x = round(source_x - feet_x)
        y = round(target_feet_y - feet_y)
    else:
        x = (size[0] - cropped.width) // 2
        y = (size[1] - cropped.height) if baseline is None else baseline - cropped.height
    canvas.alpha_composite(cropped, (x, max(0, y)))
    return canvas


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Folder of PNG frames")
    parser.add_argument("output", type=Path, help="Output folder")
    parser.add_argument("--width", type=int, required=True)
    parser.add_argument("--height", type=int, required=True)
    parser.add_argument("--columns", type=int, default=0)
    parser.add_argument("--baseline", type=int)
    parser.add_argument("--landmarks", type=Path, help="JSON mapping frame filename to head_y/feet_y/feet_x")
    parser.add_argument("--target-body-height", type=int, help="Required with --landmarks for character normalization")
    parser.add_argument("--target-pivot-x", type=int)
    args = parser.parse_args()

    if bool(args.landmarks) != bool(args.target_body_height):
        raise SystemExit("Use --landmarks and --target-body-height together")
    landmark_map = json.loads(args.landmarks.read_text()) if args.landmarks else {}

    frames = sorted(args.input.glob("*.png"))
    if not frames:
        raise SystemExit(f"No PNG frames found in {args.input}")
    args.output.mkdir(parents=True, exist_ok=True)
    normalized = []
    for index, frame_path in enumerate(frames):
        landmarks = landmark_map.get(frame_path.name) if landmark_map else None
        if args.landmarks and not landmarks:
            raise SystemExit(f"No landmarks supplied for {frame_path.name}")
        frame = place_frame(Image.open(frame_path), (args.width, args.height), args.baseline, landmarks, args.target_body_height, args.target_pivot_x)
        target = args.output / f"frame_{index:03d}.png"
        frame.save(target)
        normalized.append(frame)

    columns = args.columns or len(normalized)
    rows = (len(normalized) + columns - 1) // columns
    sheet = Image.new("RGBA", (columns * args.width, rows * args.height), (0, 0, 0, 0))
    for index, frame in enumerate(normalized):
        sheet.alpha_composite(frame, ((index % columns) * args.width, (index // columns) * args.height))
    sheet.save(args.output / "spritesheet.png")
    print(f"Normalized {len(normalized)} frames to {args.width}x{args.height}; sheet={sheet.size[0]}x{sheet.size[1]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
