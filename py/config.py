import re
from glob import glob

N = 0

MAIN_PATH = "C:/Users/JY810251/python/dailydictation"
MARKDOWN_PATH = f"{MAIN_PATH}/markdown/DailyDictation_conversation_English.md"
AUDIO_FILE = rf"{MAIN_PATH}\mp3\*.mp3"

FHD = 1920, 1080
RGB = 35, 24, 22
FONT_COLOR = 240, 240, 240

TITLE_FONT_SIZE = 70
FOOTER_FONT_SIZE = 20
SECTION_FONT_SIZE = 45


def extract_title_section():
    # Get title and section from markdown
    with open(MARKDOWN_PATH) as f:
        markdown_text = f.read()

    # Extract text by section using re
    sections = re.split(r"##\s+\d+\.\s+[^\n]+\n", markdown_text)[1:]
    titles = re.findall(r"##\s+\d+\.\s+[^\n]+", markdown_text)

    # Line Break Adjustments
    sections = [f"{section.strip()}\n" for section in sections]
    titles = [re.sub("## ", "", title) for title in titles]

    return titles, sections


def get_audio_path():
    audio_files = sorted(
        glob(AUDIO_FILE), key=lambda x: int(x.split("\\")[-1].split("-")[0])
        )
    print(len(audio_files))

    return audio_files


def check_character_count():
    # Check character count
    title_len_max, index = 0, 0
    for i, t in enumerate(titles):
        if title_len_max < len(t):
            title_len_max = len(t)
            index = i
    print(f'Title max length : {index, title_len_max}')

    title_len_min, index = 10000, 0
    for i, t in enumerate(titles):
        if title_len_min > len(t):
            title_len_min = len(t)
            index = i
    print(f'Title min length : {index, title_len_min}')

    section_len_max, index = 0, 0
    for i, t in enumerate(sections):
        if section_len_max < len(t):
            section_len_max = len(t)
            index = i
    print(f'Sectoin max length : {index, section_len_max}')

    section_len_min, index = 100000, 0
    for i, t in enumerate(sections):
        if section_len_min > len(t):
            section_len_min = len(t)
            index = i
    print(f'Section min length : {index, section_len_min}')


if __name__ == "__main__":

    titles, sections = extract_title_section()
    audio_files = get_audio_path()
    check_character_count()
