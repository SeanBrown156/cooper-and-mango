---
name: cm-aseprite-recolour
description: Recolour provisional sprites and sheets inside a Cooper & Mango WIP package with Aseprite and the embedded shared master palette; use when bringing generated or third-party art into final project colour language.
---

# CM Aseprite Recolour

Use only on assets already being actively curated in a package `wip/` folder.
Never recolour directly in `reference/`, `input/`, or `approved/`; copy or move
the candidate into WIP first and preserve the original for provenance.

## Workflow

1. Confirm the input and output are both under a package `wip/` directory.
2. Inspect the sprite at native scale and identify the intended palette subset.
3. Run:

   ```sh
   tools/aseprite/aseprite_recolour.sh \
     assets/characters/mango/wip/overworld/source.png \
     assets/characters/mango/wip/overworld/mango_recoloured.png
   ```

4. Open the result in Aseprite and check silhouette, contrast, markings,
   transparency, and cluster structure. Palette remapping is not permission
   to accept a bad silhouette or incorrect likeness.
5. Record the source, palette, output, and review state in the owning package
   manifest. Promote only the complete reviewed WIP package to `approved/`.

The tool uses Aseprite’s palette operation and the canonical palette file
`assets/palette/cooper_mango_master_palette.gpl`.

## Embedded Cooper & Mango master palette

Use this shared palette; select a smaller subset per asset rather than using all
colours indiscriminately:

```text
#FFCF7A #F0913E #C85A2E #7A3524   Mango orange
#E8C9E8 #7C4FD6 #4A2D73 #241B4A   Purple hoodie
#FFFFFF #F3ECD1 #E28FA0 #181425   Neutral / outline
#8A857A #55504A #2E2A26 #171412   Cooper black-grey
#FBF6EC #E0D6C4 #BFB29A #8A7C63   Cooper cream
#9FCDB0 #4E9873 #2E5F49 #1A3A2C   Cooper green
#F0C9A0 #C17F4A #8C4A2E           Rocky chestnut
#FBF3E8 #E2CCB9 #C9AF98 #A0937E   Rocky white
#584A3A #3E2731 #0F0015           Threat / boss
#C9A227 #8C1F28                   Threat accents
#8FD9D6 #2F8A8F #1C5559 #193C3E   Water / park
#FFE1A3 #E08A3C #A85A28 #5C3018   Autumn forest
#E8B796 #B86F50 #733E39           Rust industrial
#C0CBDC #8A8A82 #55554E #2E2E28   Metal industrial
#C28569 #8A5F3A                   Wood / earth
#C6E88F #63C74D #3E8948 #265C42   Forest foliage
#2CE8F5 #0099DB #124E89 #262B44   Bright water / sky
#E43B44 #FEE761 #C9BFE0           UI danger / reward / dust
```

Hard edges, no antialiasing, no semi-transparent fringe pixels, and no palette
drift are required before approval.
