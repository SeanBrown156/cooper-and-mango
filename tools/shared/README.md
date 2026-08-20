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
```

`slice_master_sprite_sheet.py` preserves the master canvas and writes derived
portrait, battle, and overworld region sheets with provenance sidecars.
`prepare_role_resolution.py` removes edge-connected backgrounds by default and
writes a transparent nearest-neighbour target-size candidate.
