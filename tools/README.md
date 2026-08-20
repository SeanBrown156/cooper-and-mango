# Asset tools

Skills describe the workflow and judgement. Tools are the small executable
adapters used by those skills: API clients, image processors, and validators.

## Providers and applications

- `openai/` — OpenAI Image and Sora API clients. These submit paid/limited API
  jobs only when explicitly run.
- `aseprite/` — Aseprite CLI operations for WIP-only palette work.
- `pixellab/` — discovery and validation for package-local PixelLab
  environment manifests and generation contracts.
- `shared/` — Provider-neutral canvas construction, frame normalization,
  procedural pixel motion, video frame extraction, and asset validation.

Install Python dependencies with:

```sh
python3 -m pip install -r tools/requirements.txt
```

Read the relevant skill before invoking a tool. Tools do not promote assets,
modify Godot scenes, or replace review decisions.
