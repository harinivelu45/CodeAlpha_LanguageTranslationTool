from gtts import gTTS

def text_to_speech(text):
    filename = "speech.mp3"
    tts = gTTS(text=text)
    tts.save(filename)
    return filename
