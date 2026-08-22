# PixelLab tools

PixelLab MCP performs generation. These local tools discover and validate
environment-local manifests and generated specifications before Godot
composition.

Every environment package may own one `environment_manifest.json` directly
under `assets/environments/<environment-id>/`. There is no central manifest
copy or index to edit. Discovery is the index; the manifest remains the source
of truth for generation inputs, asset IDs, bounds, variants, provenance,
review state, and generation order.

List discovered packages and manifests:

```sh
python3 tools/pixellab/discover_environment_manifests.py
```

Validate all discovered manifest identities, then run the room-specific
contract validation:

```sh
python3 tools/pixellab/validate_environment_manifests.py
python3 tools/pixellab/validate_tutorial_room_asset_spec.py
```
