# Shared asset tools

These scripts are deliberately provider-neutral and are used after generation:

```sh
python3 tools/shared/animation_canvas.py anchor.png animation_canvas.png --columns 4 --rows 1 --cell-width 24 --cell-height 16 --scale 8
python3 tools/shared/video_extract_frames.py output.mp4 frames/
python3 tools/shared/frames_normalize.py frames/ normalized/ --width 20 --height 16 --columns 4
python3 tools/shared/python_pixel_animation.py anchor.png idle/ --mode breathe --frames 4
python3 tools/shared/asset_validate.py normalized/frame_000.png --width 20 --height 16
python3 tools/shared/slice_master_sprite_sheet.py --master master.png --character cooper --variant v2 --out-root assets/characters/cooper --portrait-box 0,0,685,1024 --battle-box 700,0,1536,590 --overworld-box 700,590,1536,1024
python3 tools/shared/extract_selected_sprite_cells.py --master master.png --review-map master_review.png.json --select P01,B03,O12 --out-root assets/characters/cooper --character cooper --variant v2
python3 tools/shared/prepare_role_resolution.py --input selected.png --out prepared.png --role battle
python3 tools/shared/sprite_pipeline.py inspect assets/characters/mango/overworld/03_wip/south/superseded/python/
python3 tools/shared/sprite_pipeline.py build assets/characters/mango/overworld/03_wip/south/superseded/python/ /tmp/mango-sprite-preview --width 16 --height 20 --columns 4 --fps 8
```

`slice_master_sprite_sheet.py` preserves the master canvas and writes derived
portrait, battle, and overworld region sheets with provenance sidecars.
`prepare_role_resolution.py` removes edge-connected backgrounds by default and
writes a transparent nearest-neighbour target-size candidate.

## Deterministic Pillow prototype

`sprite_pipeline.py` is a small local CLI for repeatable inspection and frame
processing. `inspect` reports source dimensions, mode, alpha and visible bounds
as JSON. `build` reads an image sequence (or animated GIF), sorts filenames
using natural numeric order, optionally trims transparent bounds, fits frames
onto one shared canvas with nearest-neighbour resampling, and writes:

- `frame_###.png` normalized transparent frames;
- `spritesheet.png`, a transparent row-major sheet;
- `contact-sheet.png`, a checkerboard preview for reviewing transparency;
- `metadata.json`, including source order, dimensions, timing, and processing
  settings.

The tool is intentionally mechanical. It does not generate art, infer artistic
landmarks, remove arbitrary backgrounds, smooth pixel art, or approve a sprite.
Review silhouette, anchors, timing, palette and gameplay integration in the
usual WIP/Aseprite/Godot gates. Pillow is useful as dependable local machinery
behind provider outputs; it is not a replacement for PixelLab, Aseprite or
human art direction.

Install the project tooling dependencies with `python3 -m pip install -r
tools/requirements.txt`. The focused regression tests run without a game launch:

```sh
python3 -m unittest discover -s tools/tests -p 'test_*.py'
```
