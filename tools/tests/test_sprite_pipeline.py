import json
import tempfile
import unittest
from pathlib import Path

from PIL import Image

from tools.shared.sprite_pipeline import fit_frame, load_frames, make_contact_sheet, make_sheet


class SpritePipelineTests(unittest.TestCase):
    def test_fit_frame_preserves_transparency_and_uses_nearest(self):
        source = Image.new("RGBA", (5, 2), (0, 0, 0, 0))
        for x in range(1, 4):
            for y in range(2):
                source.putpixel((x, y), (255, 0, 0, 255))
        result = fit_frame(source, (8, 8), trim=True)
        self.assertEqual(result.mode, "RGBA")
        self.assertEqual(result.size, (8, 8))
        self.assertEqual(result.getchannel("A").getbbox(), (0, 1, 8, 6))

    def test_load_frames_sorts_naturally_and_reads_gif_frames(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name in ("frame_10.png", "frame_2.png"):
                Image.new("RGBA", (2, 2), (1, 2, 3, 255)).save(root / name)
            gif = root / "cycle.gif"
            Image.new("RGBA", (2, 2), (255, 0, 0, 255)).save(gif, save_all=True, append_images=[Image.new("RGBA", (2, 2), (0, 255, 0, 255))])
            frames = load_frames([root])
            self.assertEqual([frame.label for frame in frames], ["cycle.gif", "cycle.gif#frame-001", "frame_2.png", "frame_10.png"])

    def test_sheet_and_contact_sheet_dimensions_are_repeatable(self):
        frames = [Image.new("RGBA", (4, 3), (255, 255, 255, 255)) for _ in range(3)]
        self.assertEqual(make_sheet(frames, 2, (4, 3)).size, (8, 6))
        self.assertEqual(make_contact_sheet(frames, 2, 2).size, (22, 18))


if __name__ == "__main__":
    unittest.main()
