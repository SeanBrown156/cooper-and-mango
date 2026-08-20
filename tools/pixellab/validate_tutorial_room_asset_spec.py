#!/usr/bin/env python3
"""Validate the Tutorial Room environment ledger and PixelLab request contract."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SPEC_PATH = (
    ROOT
    / "assets"
    / "environments"
    / "tutorial_room_mango"
    / "environment_manifest.json"
)

spec = json.loads(SPEC_PATH.read_text())
contract = spec["technical_contract"]
tile = contract["native_tile_size_px"]

assert spec["schema_version"] == "2.0.0"
assert spec["environment_id"] == "tutorial_room_mango"
assert spec["manifest_scope"] == "environment_local"
assert (ROOT / spec["canonical_spec"]).is_file()
assert contract["view"] == "high top-down"
assert contract["projection"] == "orthographic"
assert contract["allow_oblique"] is False
assert contract["allow_isometric"] is False
assert contract["allow_perspective"] is False
assert contract["floor_object_camera_degrees"] == 90

room_px = contract["room_canvas_px"]
room_cells = contract["room_grid_cells"]
assert room_px["width"] == room_cells["width"] * tile
assert room_px["height"] == room_cells["height"] * tile

atlas = spec["atlas"]
assert atlas["output_px"]["width"] == atlas["grid_cells"]["columns"] * tile
assert atlas["output_px"]["height"] == atlas["grid_cells"]["rows"] * tile
atlas_cell_count = sum(family["count"] for family in atlas["families"])
assert atlas_cell_count <= atlas["grid_cells"]["columns"] * atlas["grid_cells"]["rows"]
for family in atlas["families"]:
    assert family["count"] == len(family["cells"]), family["id"]

tile_ids = {item["id"] for item in spec["tileset_ledger"]}
sprite_ids = set()
valid_projection_classes = {"floor_plan", "vertical_fixture", "flat_overlay"}
valid_priorities = {"P0", "P1", "P2"}

for item in spec["sprite_ledger"]:
    item_id = item["id"]
    assert item_id not in sprite_ids, f"duplicate sprite id: {item_id}"
    sprite_ids.add(item_id)
    assert item["tool"] == "create_map_object", item_id
    assert item["priority"] in valid_priorities, item_id
    assert item["projection_class"] in valid_projection_classes, item_id
    assert item["status"] == "ready_to_generate", item_id

    canvas_w, canvas_h = item["canvas_px"]
    visible_w, visible_h = item["visible_bounds_px"]
    assert canvas_w >= contract["pixel_lab_min_canvas_px"], item_id
    assert canvas_h >= contract["pixel_lab_min_canvas_px"], item_id
    assert canvas_w % tile == 0 and canvas_h % tile == 0, item_id
    assert 0 < visible_w <= canvas_w and 0 < visible_h <= canvas_h, item_id

    footprint_w, footprint_h = item["grid_footprint_cells"]
    assert footprint_w >= 0 and footprint_h >= 0, item_id
    if item["projection_class"] == "floor_plan":
        assert footprint_w > 0 and footprint_h > 0, item_id

all_ids = tile_ids | sprite_ids | {item["id"] for item in spec["lighting_ledger"]}

for placement in spec["composition_layout"]["placements"]:
    assert placement["id"] in sprite_ids, f"unknown placement sprite: {placement['id']}"
    if "cell_rect" in placement:
        cell_x, cell_y, cell_w, cell_h = placement["cell_rect"]
        pixel_x, pixel_y, pixel_w, pixel_h = placement["pixel_rect"]
        assert [pixel_x, pixel_y, pixel_w, pixel_h] == [
            cell_x * tile,
            cell_y * tile,
            cell_w * tile,
            cell_h * tile,
        ], placement["id"]
        assert cell_x >= 0 and cell_y >= 0, placement["id"]
        assert cell_x + cell_w <= room_cells["width"], placement["id"]
        assert cell_y + cell_h <= room_cells["height"], placement["id"]

batch_ids = set()
ordered_batches = sorted(spec["generation_batches"], key=lambda batch: batch["order"])
assert [batch["order"] for batch in ordered_batches] == list(range(1, len(ordered_batches) + 1))
for batch in ordered_batches:
    for item_id in batch["items"]:
        assert item_id in all_ids, f"unknown batch item: {item_id}"
        assert item_id not in batch_ids, f"item appears in multiple batches: {item_id}"
        batch_ids.add(item_id)
assert batch_ids == all_ids, f"unbatched items: {sorted(all_ids - batch_ids)}"

print(
    "Tutorial Room generation manifest valid: "
    f"{atlas_cell_count} atlas cells, {len(tile_ids)} tileset jobs, "
    f"{len(sprite_ids)} sprite jobs, {len(spec['lighting_ledger'])} lighting states"
)
print("Room: 512x384 px / 32x24 cells; strict orthographic high top-down")
