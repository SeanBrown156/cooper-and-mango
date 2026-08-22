#!/usr/bin/env python3
"""Deterministic, provider-neutral inspection and sprite-sheet utilities.

This tool performs mechanical image operations only. It does not generate art,
guess landmarks, or remove backgrounds beyond transparent-pixel trimming when
explicitly requested.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

try:
    from PIL import Image, ImageDraw, ImageSequence
except ImportError as exc:  # pragma: no cover - dependency diagnostic
    raise SystemExit("Install Pillow first: python3 -m pip install -r tools/requirements.txt") from exc


IMAGE_SUFFIXES = {".gif", ".jpeg", ".jpg", ".png", ".webp"}
RESAMPLING = Image.Resampling.NEAREST


@dataclass(frozen=True)
class Frame:
    path: Path
    index: int
    image: Image.Image
    source_mode: str
    source_has_alpha: bool

    @property
    def label(self) -> str:
        return self.path.name if self.index == 0 else f"{self.path.name}#frame-{self.index:03d}"


def natural_key(path: Path) -> tuple[object, ...]:
    return tuple(int(part) if part.isdigit() else part.casefold() for part in re.split(r"(\d+)", path.name))


def image_paths(inputs: Iterable[Path]) -> list[Path]:
    paths: list[Path] = []
    for item in inputs:
        if item.is_dir():
            paths.extend(path for path in item.iterdir() if path.is_file() and path.suffix.casefold() in IMAGE_SUFFIXES)
        elif item.is_file() and item.suffix.casefold() in IMAGE_SUFFIXES:
            paths.append(item)
        else:
            raise SystemExit(f"No supported image input: {item}")
    return sorted(set(paths), key=natural_key)


def load_frames(inputs: Iterable[Path]) -> list[Frame]:
    frames: list[Frame] = []
    for path in image_paths(inputs):
        with Image.open(path) as source:
            for index, source_frame in enumerate(ImageSequence.Iterator(source)):
                source_mode = source_frame.mode
                has_alpha = "A" in source_mode or "transparency" in source.info
                frames.append(Frame(path, index, source_frame.convert("RGBA"), source_mode, has_alpha))
    if not frames:
        raise SystemExit("No image frames found")
    return frames


def alpha_bbox(image: Image.Image) -> list[int] | None:
    bbox = image.getchannel("A").getbbox()
    return list(bbox) if bbox else None


def inspect_records(frames: Iterable[Frame]) -> list[dict[str, object]]:
    records = []
    for frame in frames:
        records.append({
            "frame": frame.label,
            "source": str(frame.path),
            "source_frame": frame.index,
            "dimensions": list(frame.image.size),
            "mode": frame.source_mode,
            "has_alpha": frame.source_has_alpha,
            "visible_bbox": alpha_bbox(frame.image),
        })
    return records


def fit_frame(source: Image.Image, size: tuple[int, int], trim: bool) -> Image.Image:
    source = source.convert("RGBA")
    if trim:
        bbox = source.getchannel("A").getbbox()
        if bbox:
            source = source.crop(bbox)
        else:
            return Image.new("RGBA", size, (0, 0, 0, 0))
    scale = min(size[0] / source.width, size[1] / source.height)
    resized_size = (max(1, round(source.width * scale)), max(1, round(source.height * scale)))
    if resized_size != source.size:
        source = source.resize(resized_size, RESAMPLING)
    canvas = Image.new("RGBA", size, (0, 0, 0, 0))
    canvas.alpha_composite(source, ((size[0] - source.width) // 2, (size[1] - source.height) // 2))
    return canvas


def make_sheet(frames: list[Image.Image], columns: int, cell_size: tuple[int, int]) -> Image.Image:
    rows = (len(frames) + columns - 1) // columns
    sheet = Image.new("RGBA", (columns * cell_size[0], rows * cell_size[1]), (0, 0, 0, 0))
    for index, frame in enumerate(frames):
        sheet.alpha_composite(frame, ((index % columns) * cell_size[0], (index // columns) * cell_size[1]))
    return sheet


def make_contact_sheet(frames: list[Image.Image], columns: int, scale: int, gap: int = 2) -> Image.Image:
    width = max(frame.width for frame in frames) * scale
    height = max(frame.height for frame in frames) * scale
    rows = (len(frames) + columns - 1) // columns
    sheet = Image.new("RGB", (columns * width + (columns + 1) * gap, rows * height + (rows + 1) * gap), (42, 42, 42))
    draw = ImageDraw.Draw(sheet)
    for index, frame in enumerate(frames):
        x = gap + (index % columns) * (width + gap)
        y = gap + (index // columns) * (height + gap)
        for tile_y in range(0, height, 8):
            for tile_x in range(0, width, 8):
                colour = (224, 224, 224) if ((tile_x // 8) + (tile_y // 8)) % 2 == 0 else (180, 180, 180)
                draw.rectangle((x + tile_x, y + tile_y, x + min(tile_x + 7, width - 1), y + min(tile_y + 7, height - 1)), fill=colour)
        preview = frame.resize((frame.width * scale, frame.height * scale), RESAMPLING)
        sheet.paste(preview, (x + (width - preview.width) // 2, y + (height - preview.height) // 2), preview)
    return sheet


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n")


def command_inspect(args: argparse.Namespace) -> int:
    records = inspect_records(load_frames(args.input))
    payload = {"tool": "sprite_pipeline", "operation": "inspect", "frames": records}
    rendered = json.dumps(payload, indent=2) + "\n"
    if args.json:
        write_json(args.json, payload)
    print(rendered, end="")
    return 0


def command_build(args: argparse.Namespace) -> int:
    source_frames = load_frames(args.input)
    cell_size = (args.width, args.height)
    normalized = [fit_frame(frame.image, cell_size, args.trim) for frame in source_frames]
    args.output.mkdir(parents=True, exist_ok=True)
    for index, frame in enumerate(normalized):
        frame.save(args.output / f"frame_{index:03d}.png", format="PNG", optimize=False)
    columns = args.columns or len(normalized)
    sheet = make_sheet(normalized, columns, cell_size)
    contact = make_contact_sheet(normalized, columns, args.preview_scale)
    sheet.save(args.output / "spritesheet.png", format="PNG", optimize=False)
    contact.save(args.output / "contact-sheet.png", format="PNG", optimize=False)
    metadata = {
        "tool": "sprite_pipeline",
        "operation": "build",
        "source_frames": inspect_records(source_frames),
        "frame_order": [frame.label for frame in source_frames],
        "output_dimensions": list(cell_size),
        "frame_count": len(normalized),
        "columns": columns,
        "rows": (len(normalized) + columns - 1) // columns,
        "sprite_sheet": "spritesheet.png",
        "contact_sheet": "contact-sheet.png",
        "timing": {"fps": args.fps, "frame_duration_ms": round(1000 / args.fps)},
        "normalization": {"fit": "contain", "trim_transparent_bounds": args.trim, "resampling": "nearest-neighbour"},
        "review_boundary": "Mechanical output only; inspect silhouette, landmarks, timing and palette before approval.",
    }
    write_json(args.output / "metadata.json", metadata)
    print(f"Built {len(normalized)} frames, {sheet.width}x{sheet.height} sprite sheet, and contact sheet in {args.output}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    inspect_parser = subparsers.add_parser("inspect", help="Report dimensions, alpha and visible bounds as JSON")
    inspect_parser.add_argument("input", nargs="+", type=Path)
    inspect_parser.add_argument("--json", type=Path, help="Also write the report to this path")
    inspect_parser.set_defaults(function=command_inspect)

    build_parser = subparsers.add_parser("build", help="Normalize frames and write sheets plus metadata")
    build_parser.add_argument("input", nargs="+", type=Path)
    build_parser.add_argument("output", type=Path)
    build_parser.add_argument("--width", type=int, required=True)
    build_parser.add_argument("--height", type=int, required=True)
    build_parser.add_argument("--columns", type=int, default=0)
    build_parser.add_argument("--fps", type=float, default=8.0)
    build_parser.add_argument("--preview-scale", type=int, default=4)
    build_parser.add_argument("--trim", action="store_true", help="Crop transparent bounds before fitting")
    build_parser.set_defaults(function=command_build)

    args = parser.parse_args()
    if args.command == "build" and (args.width < 1 or args.height < 1 or args.fps <= 0 or args.preview_scale < 1):
        parser.error("build dimensions, fps and preview scale must be positive")
    if args.command == "build" and args.columns < 0:
        parser.error("--columns cannot be negative")
    return args.function(args)


if __name__ == "__main__":
    raise SystemExit(main())
