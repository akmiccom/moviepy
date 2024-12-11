from config import input_text
from moviepy import TextClip


def text_clip():
    font = "resources/font/font.ttf"
    clip_text = TextClip(
        font=font,
        text=input_text,
        font_size=70,
        color="white",
        size=(1920, None),
        text_align="left",
    )

    print("TextClip is complete!")

    return clip_text


if __name__ == "__main__":
    text_clip()
