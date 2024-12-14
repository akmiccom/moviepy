from moviepy import ColorClip
from config import FHD, RGB


# ColorClip(size, color=None, is_mask=False, duration=None)

def create_color_clip():
    color_clip = ColorClip(FHD, color=RGB, is_mask=False, duration=None)

    print(f"ColorClip size: {color_clip.size}")
    print("--ColorClip have been created.--")

    return color_clip


if __name__ == "__main__":
    color_clip = create_color_clip()
