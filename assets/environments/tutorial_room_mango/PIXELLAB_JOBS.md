# PixelLab room build jobs

These are provisional generation jobs for the blended Gemini living-room /
bedroom composition. The real-room photos guide object identity and materials;
they do not replace the composite layout.

| Job | PixelLab ID | Scope | Status at kickoff |
|---|---|---|---|
| Connected tileset | `b2bc2950-0288-40b9-933e-e360adba4da0` | 16px warm timber floor to cream geometric rug transition | completed |
| Building kit | `d46173af-0410-4a60-8a7d-373815bfdb63` | 16px timber floor, plaster walls, baseboard, doorways and shell pieces | completed |
| Object batch A | `c90c041d-dca4-4b51-a4f2-1c8bd821f42a` | deep-blue futon, dining/work table, cane chair, carved chest | reviewed; four objects selected |
| Object batch B | `fd3b8e60-8b66-41ad-9deb-1dcaa41301a5` | Noguchi pendant, green cat tree, hanging plant, potted plant | reviewed; four objects selected |
| Object batch C | `4ec91633-e075-4388-ad9a-3e8f649ffbd9` | TV console, workstation, clothes rack, wire shelving | reviewed; four objects selected |
| Object batch D | `cb983471-9cff-47cb-ae2d-d7a87699d589` | geometric rug, pet bed, metal bowl, lidded wastebasket/shoe storage | reviewed; four objects selected |

Selected object IDs:

- Batch A: `a1427641-b49c-4a35-a8ff-f879e543422a`, `0fb6c29a-f915-4c02-b673-db4fca2e5f97`, `e8755e4e-5bd4-4ced-a7f7-397272f11514`, `a47b56b6-6906-44cc-92cf-a505eed175a3`
- Batch B: `c2d02895-4660-41a6-9d47-a822b7e67272`, `5f712341-2ce5-4957-809c-63a6cf61f2b3`, `0866c25b-ceeb-4a14-8cae-8fe2d5564bea`, `d11a834f-a01b-45da-844a-5f3ccc8a0200`
- Batch C: `2262a8db-bc42-4f5e-95d4-cc98778b8855`, `685bfb10-cae8-482b-a483-8841ebb581a8`, `37ed6051-33ab-4c89-88eb-22352be07234`, `7285179d-5ee9-411f-8ff3-20aa0aa5a005`
- Batch D: `309367b5-563d-4b01-95bf-e71544fe497d`, `ef9b6e1e-2b60-4095-baa7-cd3721f1cb59`, `9b299bd6-2e52-4ff1-9baf-f005baee9e9f`, `920a4c8e-10f3-4d63-a9b6-1fb2dda9069a`

Review completed results with the matching PixelLab `get_*` call before
selecting frames or importing anything into `wip/`. Do not promote generated
art directly to `approved/`; first check 16px grid readability, palette,
silhouette, collision footprint, and visual fit against the Gemini composites.

## Strict-size replacement attempt

The following replacement batch used the canonical native bounds and explicit
orthographic high top-down prompts. It is downloaded under
`wip/pixellab/topdown/`. Only the flat, non-oblique subset is now wired through
`scenes/rooms/tutorial_room_mango_pixellab_props.tscn`; failed furniture remains
hidden until a replacement passes visual review. Correct canvas dimensions
alone are not sufficient.

Wired from this batch: geometric rug, paper pendant, potted floor plant, clothes
rack, metal pet bowl, and lidded wastebasket. The hanging plant and pet bed are
also hidden because their silhouettes were not reliably overhead.

| Asset | Native bounds | PixelLab ID |
|---|---:|---|
| Futon sofa-bed | 112×64 | `e8beee3c-f1a2-4379-a5ff-24cd6948fe1e` |
| Geometric rug | 144×96 | `33bc917c-1236-4d3e-8a15-8976fbf495b7` |
| Dining table | 64×48 | `c22ab2f2-0b05-4c3c-8cd9-90b77642b1ac` |
| Cane chair | 32×32 | `b66c9d9a-c8fc-41e6-b09f-a27b87b32e10` |
| Carved chest | 64×32 | `6b1d4bba-489a-4113-bf9b-012771aa7d36` |
| Cat tree | 64×96 | `2dc7bc9f-7e7d-4331-bbc9-721efc1579ec` |
| TV console | 80×48 | `291848c5-f3a8-4935-a764-6b91876ea7a4` |
| Desk | 64×48 | `13a3812b-d619-4086-997b-f1e5869a0b78` |
| Pendant, plants, rack, shelving, pet props | canonical bounds | IDs in the topdown export folder |

Review outcome: size contract passed; orientation contract failed for the
PixelLab map-object model on the furniture anchors. Keep the failed originals as
evidence, not runtime art.

## Background orientation retry

These retries were queued with exact canonical bounds, high top-down view, flat
shading, and explicit 90-degree/floor-plan constraints. They are not wired
until visual review confirms that no visible side faces were drawn. Completed
exports are saved under `wip/pixellab/topdown_retry/`.

| Asset | Native bounds | PixelLab ID | Status |
|---|---:|---|---|
| Futon sofa-bed | 112×64 | `d7d746d6-7903-4c74-af4e-0b5c0f2cd9c9` | completed; failed visual review |
| Dining/work table | 64×48 | `54023036-1e27-453b-b083-ad40f3236b12` | completed; failed visual review |
| Cane dining chair | 32×32 | `dcc29ef2-abe1-421b-8bb7-7bc8c3bdd889` | completed; failed visual review |
| Carved storage chest | 64×32 | `a8c85278-31a7-4703-aad7-2364d7defb14` | completed; failed visual review |
| Green cat tree | 64×96 | `0e3aecce-a513-45cd-8f40-fd1ed3059fbc` | completed; failed visual review |
| TV/media console | 80×48 | `36a7503e-9a0f-4f5b-a66b-aab4bec107fd` | completed; failed visual review |
| Desk workstation | 64×48 | `1ca9ba11-0e85-4f75-a264-f22e9014deff` | completed; failed visual review |
| Pet bed | 48×32 | `977665a5-8d1f-4b29-a1ab-993d5a40092e` | completed; failed visual review |
| Wire shelving | 64×64 | `100d7054-2a56-4219-a3c0-b651bb31cf48` | completed; failed visual review |
