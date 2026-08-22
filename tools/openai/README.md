# OpenAI tools

These are explicit adapters for OpenAI Image and Sora. Load the project
`.env.local` before live calls.

```sh
python3 tools/openai/image_generate.py --prompt-file prompt.txt --out output.png
python3 tools/openai/video_generate.py create --prompt "..."
python3 tools/openai/video_generate.py poll video_... --out output.mp4
```
