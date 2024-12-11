import os

path = "C:/Users/JY810251/ffmpeg-master-latest-win64-gpl-shared/bin"
os.environ["FFMPEG_BINARY"] = f"{path}/ffmpeg.exe"
os.environ["FFPLAY_BINARY"] = f"{path}/ffplay.exe"

str_filename = "str/subtitle.srt"
audio_filename = "mp3/output.mp3"
background_filename = "mp4/background.mp4"
video_filename = "mp4/output.mp4"

# font = "resources/font/font.ttf"

input_text = '''
Where is Jane?
She is in the living room.
What is she doing?
She is playing the piano.
Where is the car?
It is in the garage.
Where is the dog?
The dog is in front of the door.
What is the dog doing?
The dog is eating.
'''
