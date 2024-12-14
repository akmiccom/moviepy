from config import N, FHD, FONT_COLOR
from config import TITLE_FONT_SIZE, FOOTER_FONT_SIZE, SECTION_FONT_SIZE
from config import extract_title_section
from moviepy import TextClip

# TextClip(
#     font, text=None, filename=None, font_size=None, size=(None, None),
#     margin=(None, None), color="black", bg_color=None, stroke_color=None,
#     stroke_width=0, method="label", text_align="left",
#     horizontal_align="center", vertical_align="center", interline=4,
#     transparent=True, duration=None,
# )

FONT = "font/MONOS.ttf"


def create_text_clip(title, footer, section):

    # Title
    title_clip = TextClip(
        FONT,
        text=title,
        font_size=TITLE_FONT_SIZE,
        margin=(30, 30),
        color="white",
        # color=FONT_COLOR,
        )

    # Footer
    footer_clip = TextClip(
        FONT,
        text=footer,
        font_size=FOOTER_FONT_SIZE,
        margin=(10, 10),
        # color="white",
        color=(190, 190, 190),
        )

    # Section
    M_LEFT, M_TOP, M_RIGHT, M_BTM = 50, 50, 30, 0
    INTER_LINE = 50
    section_clip = TextClip(
        FONT,
        text=section,
        font_size=SECTION_FONT_SIZE,
        size=(FHD[0]-M_LEFT-M_RIGHT, None),
        method="caption",
        margin=(M_LEFT, M_TOP, M_RIGHT, M_BTM),
        # color="white",
        color=FONT_COLOR,
        interline=INTER_LINE,
        )

    text_clip = title_clip, footer_clip, section_clip

    print(f'Number of text_clip : {len(text_clip)}')
    print("--TextClip have been created.--")

    return text_clip


if __name__ == "__main__":

    titles, sections = extract_title_section()

    title = titles[N]
    section = sections[N]
    footer = "akmiccom@gmail.com"

    # Check
    text_clip = create_text_clip(title, footer, section)
    for clip in text_clip:
        clip.show()
