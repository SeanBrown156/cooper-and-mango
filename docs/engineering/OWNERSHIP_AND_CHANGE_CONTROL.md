# Documentation ownership and change control

`docs/README.md` is the navigation index. Each document listed there is the
source of truth for its own subject; avoid copying decisions into other docs.

## Ownership

- Vision and narrative: Sean and Lillian
- Art direction and asset approval: Sean and Lillian
- Design and content schema: Sean, with implementation support from Codex/Claude
- Engineering and MCP/tooling: the implementation agent, reviewed in the running project
- Audio direction: Sean and Lillian
- Production and QA: Sean, validated against the current vertical-slice criteria

## Change rules

1. Update the source-of-truth document first.
2. Update affected implementation guidance or code comments in the same change.
3. Use links to the source document instead of repeating the decision.
4. Record structural documentation changes in [`CHANGELOG.md`](../../CHANGELOG.md).
5. Keep `README.md` as the public project landing page, `CLAUDE.md` as the agent startup guide, and `docs/README.md` as the documentation index.

## Authority order

When documents disagree, use this order:

1. approved human decisions and canonical assets;
2. the relevant source-of-truth document in `docs/`;
3. implementation guidance and tool notes;
4. generated or provisional material.
