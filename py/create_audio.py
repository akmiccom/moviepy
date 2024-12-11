from config import input_text, audio_filename
from gtts import gTTS


tts = gTTS(text=input_text, lang='en')
tts.save(audio_filename)

print("Audio files have been created.")
