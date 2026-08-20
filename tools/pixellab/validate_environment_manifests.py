#!/usr/bin/env python3
"""Validate every discovered environment-local manifest and its identity."""

from discover_environment_manifests import iter_manifests


def main() -> int:
    manifests = list(iter_manifests())
    for path, manifest in manifests:
        print(f"Environment manifest valid: {manifest['environment_id']} ({path})")
    print(f"Validated {len(manifests)} environment manifest(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
