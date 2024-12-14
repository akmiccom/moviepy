from config import N, get_audio_path
from moviepy import AudioFileClip
import os


# AudioFileClip(
#     filename, decode_file=False, buffersize=200000, nbytes=2, fps=44100
#     )

def create_audio_clip(audio):

    audio_clip = AudioFileClip(audio, buffersize=200000, nbytes=2, fps=44100)

    print(f"Audio file: {audio}")
    file_name = os.path.splitext(os.path.basename(audio))[0]
    print(f"Audio Duration: {audio_clip.duration} seconds")
    print("--Audio_clip have been created.--")

    return audio_clip, file_name


if __name__ == "__main__":

    audio_files = get_audio_path()
    audio_file = audio_files[N]
    audio_clip, file_name = create_audio_clip(audio_file)
