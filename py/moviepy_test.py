import os
os.environ["FFMPEG_BINARY"] = f"C:/Users/JY810251/ffmpeg-master-latest-win64-gpl-shared/bin/ffmpeg.exe"
os.environ["FFPLAY_BINARY"] = f"C:/Users/JY810251/ffmpeg-master-latest-win64-gpl-shared/bin/ffplay.exe"


from moviepy import *
from gtts import gTTS


text = "How are you? I'm good. Thank you for asking. How about you?"

str_file = "str/subtitle.srt"
audio_file = "mp3/output.mp3"
video_file = "mp4/output.mp4"

# # create audio
tts = gTTS(text=text, lang='en')
# tts.save(audio_file)
# audio = AudioFileClip(audio_file)

# create text
font = "resources/font/font.ttf"
intro_text = TextClip(
    font=font,
    text=text,
    font_size=50,
    color="#fff",
    text_align="center",
)

intro_text = intro_text.with_duration(5)

background = ColorClip(size=(1920, 1080), color=(0, 0, 0), duration=audio.duration)
backgroundvideo = background.with_audio(audio)

video = CompositeVideoClip([backgroundvideo, intro_text])

# video.preview(fps=10)
video.write_videofile(video_file, fps=24, codec="libx264")
