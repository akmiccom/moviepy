from config import get_audio_path, extract_title_section
from audio_clip import create_audio_clip
from color_clip import create_color_clip
from text_clip import create_text_clip
from Composite_video import composite_video_clip


def main(fps=1, start=0, stop=2):

    footer = "akmiccom@gmail.com"
    audio_files = get_audio_path()
    titles, sections = extract_title_section()
    color_clip = create_color_clip()

    for i, audio_file in enumerate(audio_files):
        if i < start-1:
            continue
        if i > stop-1:
            break

        audio_clip, file_name = create_audio_clip(audio_file)
        text_clip = create_text_clip(titles[i], footer, sections[i])
        video = composite_video_clip(audio_clip, color_clip, text_clip)

        mp4_path = f"mp4/{file_name}.mp4"
        video.write_videofile(mp4_path, fps=fps, codec="libx264")


if __name__ == "__main__":
    main(fps=20, start=6, stop=100)
