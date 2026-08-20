#!/usr/bin/env python3
"""Generate or edit an image candidate with the OpenAI Image API."""

from __future__ import annotations

import argparse
import base64
import json
import os
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prompt")
    parser.add_argument("--prompt-file", type=Path)
    parser.add_argument("--model", default="gpt-image-2")
    parser.add_argument("--size", default="1024x1024")
    parser.add_argument("--quality", default="medium", choices=("low", "medium", "high", "auto"))
    parser.add_argument(
        "--background",
        default="opaque",
        choices=("opaque",),
        help="OpenAI image background mode; sprite generations must remain opaque (white is specified in the prompt).",
    )
    parser.add_argument("--image", action="append", type=Path, help="Reference image; switches to edit mode")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if bool(args.prompt) == bool(args.prompt_file):
        raise SystemExit("Provide exactly one of --prompt or --prompt-file")
    prompt = args.prompt if args.prompt else args.prompt_file.read_text()
    if not os.environ.get("OPENAI_API_KEY"):
        raise SystemExit("OPENAI_API_KEY is not set; load the project .env.local before running")
    try:
        from openai import OpenAI
    except ImportError as exc:  # pragma: no cover
        raise SystemExit("Install the OpenAI SDK: python3 -m pip install openai") from exc

    client = OpenAI()
    if args.image:
        result = client.images.edit(
            model=args.model,
            image=[image.open("rb") for image in args.image],
            prompt=prompt,
            size=args.size,
            quality=args.quality,
            background=args.background,
        )
        mode = "edit"
    else:
        result = client.images.generate(
            model=args.model,
            prompt=prompt,
            size=args.size,
            quality=args.quality,
            background=args.background,
        )
        mode = "generate"
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_bytes(base64.b64decode(result.data[0].b64_json))
    metadata = args.out.with_suffix(args.out.suffix + ".json")
    metadata.write_text(json.dumps({"provider": "openai", "mode": mode, "model": args.model, "prompt": prompt, "size": args.size, "quality": args.quality, "background": args.background, "output": str(args.out)}, indent=2) + "\n")
    prompt_sidecar = args.out.with_suffix(args.out.suffix + ".prompt.md")
    prompt_sidecar.write_text(
        "# Generation prompt\n\n"
        f"- Provider: OpenAI\n"
        f"- Model: `{args.model}`\n"
        f"- Mode: `{mode}`\n"
        f"- Size: `{args.size}`\n"
        f"- Quality: `{args.quality}`\n"
        f"- Background: `{args.background}`\n"
        f"- Metadata: [{metadata.name}]({metadata.name})\n\n"
        "## Prompt\n\n"
        f"{prompt.rstrip()}\n"
    )
    print(f"Wrote {args.out}, {metadata}, and {prompt_sidecar}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
