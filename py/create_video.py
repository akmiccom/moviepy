from config import *
from moviepy import *


audio = AudioFileClip(audio_filename)

background = ColorClip(
    size=(1920, 1080),
    color=(0, 0, 0),
    duration=audio.duration
    )

background.write_videofile(
    background_filename, fps=24, codec="libx264"
    )
