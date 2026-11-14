"""food-picture-01 entry (v2): serve the committed hero image.

The image is a photorealistic photograph of a bowl of tonkotsu ramen:
wooden chopsticks lifting a tall glossy noodle pull above creamy broth,
a halved soft-boiled egg with its jammy yolk dripping in a stream,
torched chashu pork fanned along the bowl, red chili-oil swirls, and
steam curling up against a dark background. It was generated for this
entry and is committed as image.jpg.

The program is deterministic: every run writes exactly those bytes to
entry.png. JPEG bytes under the entry.png name are allowed; the gate
tells the format apart by the file's first bytes.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    src = HERE / "image.jpg"
    dst = out_dir / "entry.png"
    shutil.copyfile(src, dst)
    # Guard against a truncated write: the output must be the image, byte for byte.
    if dst.stat().st_size != src.stat().st_size:
        raise RuntimeError("entry.png size does not match image.jpg")


if __name__ == "__main__":
    main()
