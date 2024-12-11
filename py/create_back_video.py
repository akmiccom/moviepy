from config import audio_filename, background_filename
from moviepy import AudioFileClip, ColorClip


audio = AudioFileClip(audio_filename)

background = ColorClip(
    size=(1920, 1080),
    color=(30, 30, 30),
    duration=audio.duration
    )

background.write_videofile(
    background_filename, fps=24, codec="libx264"
    )

print("Background video files have been created.")
