#!/usr/bin/env python3
"""Validate the native-size contract used for Tutorial Room PixelLab prompts."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "tools/pixellab_tutorial_room_spec.json"

spec = json.loads(SPEC.read_text())
tile = spec["native_tile_size_px"]
generation = spec["default_generation"]
assert generation["view"] == "high top-down"
assert generation["projection"] == "orthographic"
assert generation["allow_oblique"] is False
assert generation["allow_isometric"] is False
assert generation["content_must_fit_native_bounds"] is True
for name, bounds in spec["object_bounds_px"].items():
    width, height = bounds
    assert width >= tile * 2 and height >= tile * 2, f"{name}: below 32px API minimum"
    assert width % tile == 0 and height % tile == 0, f"{name}: not aligned to {tile}px grid"
print(f"Tutorial Room PixelLab contract valid: {len(spec['object_bounds_px'])} object bounds")
print("Default: native 16px grid, orthographic high top-down, oblique/isometric forbidden")
