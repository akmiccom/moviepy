from config import N, get_audio_path, extract_title_section
from audio_clip import create_audio_clip
from color_clip import create_color_clip
from text_clip import create_text_clip
from moviepy import CompositeVideoClip
from moviepy import vfx


def composite_video_clip(audio_clip, color_clip, text_clip):

    video_duration = audio_clip.duration + 4
    # print(video_duration)

    # with_audio
    color_clip = color_clip.with_duration(video_duration)
    video_clip = color_clip.with_audio(audio_clip)
    # print(video_clip.start, video_clip.end)

    title_clip = text_clip[0].with_start(0).with_end(10)
    title_clip = title_clip.with_effects([vfx.FadeIn(0), vfx.FadeOut(3)])
    title_clip = title_clip.with_position(("center", "top"))
    # print(title_clip.start, title_clip.end)

    footer_clip = text_clip[1].with_start(0).with_end(10)
    footer_clip = footer_clip.with_position(("right", "bottom"))
    footer_clip = footer_clip.with_effects([vfx.FadeIn(0), vfx.FadeOut(3)])

    section_clip = text_clip[2].with_start(1).with_end(video_duration - 1)
    section_clip = section_clip.with_effects([vfx.FadeIn(1), vfx.FadeOut(3)])
    # print(section_clip.start, section_clip.end)

    START_POSITION = 900
    SPEED_PARAMETER = 1.4
    init_speed = section_clip.h / video_duration * SPEED_PARAMETER
    section_clip = section_clip.with_position(
        lambda t: ("center", START_POSITION - t * int(init_speed))
    )

    video = CompositeVideoClip(
        [video_clip, title_clip, footer_clip, section_clip]
        )

    print(f'{video.duration:.02f}')
    print("--CompositeVideoClip have been created.--")

    return video


if __name__ == "__main__":

    audio_files = get_audio_path()
    titles, sections = extract_title_section()

    audio_file = audio_files[N]
    title = titles[N]
    section = sections[N]
    footer = "akmiccom@gmail.com"

    audio_clip, file_name = create_audio_clip(audio_file)
    color_clip = create_color_clip()
    text_clip = create_text_clip(title, footer, section)

    video = composite_video_clip(audio_clip, color_clip, text_clip)
