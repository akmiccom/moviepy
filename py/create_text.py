from config import *
from moviepy import *


# create text
output_text = TextClip(
    font=font,
    text=input_text,
    font_size=50,
    color="white",
    size=(1920, None),
    text_align="left",
)


print(f"TextClip is complete!")