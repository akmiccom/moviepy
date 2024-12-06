from gtts import gTTS

text = "How are you? I'm good. Thank you for asking. How about you?"

tts = gTTS(text=text, lang='en')

tts.save("mp3/output.mp3")

print("音声ファイル 'output.mp3' が作成されました。")