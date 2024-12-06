from gtts import gTTS
from config import *


tts = gTTS(text=input_text, lang='en')

tts.save(audio_filename)

print(f"Audio files have been created.")