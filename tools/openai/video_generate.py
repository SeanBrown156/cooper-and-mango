#!/usr/bin/env python3
"""Create, poll, and download a reference-guided OpenAI video job."""

from __future__ import annotations

import argparse
import os
import time
from pathlib import Path


def client():
    if not os.environ.get("OPENAI_API_KEY"):
        raise SystemExit("OPENAI_API_KEY is not set; load the project .env.local before running")
    try:
        from openai import OpenAI
    except ImportError as exc:  # pragma: no cover
        raise SystemExit("Install the OpenAI SDK: python3 -m pip install openai") from exc
    return OpenAI()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    create = sub.add_parser("create")
    create.add_argument("--prompt", required=True)
    create.add_argument("--model", default="sora-2", choices=("sora-2", "sora-2-pro"))
    create.add_argument("--size", default="1280x720")
    create.add_argument("--seconds", default="4", choices=("4", "8", "12"))
    create.add_argument("--reference", type=Path)
    poll = sub.add_parser("poll")
    poll.add_argument("video_id")
    poll.add_argument("--out", type=Path)
    poll.add_argument("--interval", type=int, default=10)
    args = parser.parse_args()
    api = client()

    if args.command == "create":
        params = {"model": args.model, "prompt": args.prompt, "size": args.size, "seconds": args.seconds}
        if args.reference:
            params["input_reference"] = args.reference.open("rb")
        video = api.videos.create(**params)
        print(f"{video.id}\t{video.status}")
        return 0

    video = api.videos.retrieve(args.video_id)
    while video.status in ("queued", "in_progress"):
        print(f"{video.id}: {video.status} {getattr(video, 'progress', 0)}%")
        time.sleep(args.interval)
        video = api.videos.retrieve(video.id)
    if video.status != "completed":
        raise SystemExit(f"Video job {video.id} ended with status {video.status}: {getattr(video, 'error', None)}")
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        content = api.videos.download_content(video.id)
        args.out.write_bytes(content.read())
        print(f"Wrote {args.out}")
    else:
        print(f"completed: {video.id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
