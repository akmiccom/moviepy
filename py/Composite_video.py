from config import audio_filename, background_filename, video_filename
from moviepy import AudioFileClip, VideoFileClip, CompositeVideoClip
from create_text import text_clip


audio = AudioFileClip(audio_filename)

background_video = VideoFileClip(background_filename)
background_video = background_video.with_audio(audio)

clip_text = text_clip()
# clip_text = clip_text.with_position("center")
clip_text = clip_text.with_position(lambda t: ("center", 1080+200 - t * 100))
clip_text = clip_text.with_duration(audio.duration)

video = CompositeVideoClip([background_video, clip_text])
# video.preview(fps=10)
video.write_videofile(video_filename, fps=24, codec="libx264")
