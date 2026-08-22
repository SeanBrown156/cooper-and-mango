#!/usr/bin/env python3
"""Discover environment-local manifests without creating a central ledger."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[2]
ENVIRONMENTS_ROOT = ROOT / "assets" / "environments"
MANIFEST_NAME = "environment_manifest.json"


def discover_manifest_paths(
    environments_root: Path = ENVIRONMENTS_ROOT,
) -> list[Path]:
    """Return manifests owned directly by environment package directories."""

    if not environments_root.is_dir():
        return []
    return sorted(
        path
        for package in environments_root.iterdir()
        if package.is_dir() and package.name != "shared"
        for path in [package / MANIFEST_NAME]
        if path.is_file()
    )


def load_manifest(path: Path) -> dict:
    """Load a manifest and require the local-package identity fields."""

    data = json.loads(path.read_text())
    if not isinstance(data, dict):
        raise ValueError(f"manifest must contain a JSON object: {path}")
    if data.get("manifest_scope") != "environment_local":
        raise ValueError(f"manifest is not environment-local: {path}")
    if data.get("environment_id") != path.parent.name:
        raise ValueError(
            f"environment_id {data.get('environment_id')!r} does not match "
            f"owning package {path.parent.name!r}: {path}"
        )
    return data


def iter_manifests(
    environments_root: Path = ENVIRONMENTS_ROOT,
) -> Iterable[tuple[Path, dict]]:
    for path in discover_manifest_paths(environments_root):
        yield path, load_manifest(path)


def resolve_manifest(
    environment_id: str,
    environments_root: Path = ENVIRONMENTS_ROOT,
) -> Path:
    """Resolve an environment ID through package discovery."""

    matches = [
        path
        for path in discover_manifest_paths(environments_root)
        if path.parent.name == environment_id
    ]
    if not matches:
        raise FileNotFoundError(
            f"no {MANIFEST_NAME} found for environment {environment_id!r}"
        )
    if len(matches) > 1:
        raise ValueError(f"multiple manifests found for {environment_id!r}")
    load_manifest(matches[0])
    return matches[0]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--environment-id",
        help="only report the package for this environment ID",
    )
    args = parser.parse_args()

    paths = discover_manifest_paths()
    if args.environment_id:
        paths = [resolve_manifest(args.environment_id)]
    for path in paths:
        manifest = load_manifest(path)
        print(f"{manifest['environment_id']}\t{path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
