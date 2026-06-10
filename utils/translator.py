from deep_translator import GoogleTranslator
from langdetect import detect

def translate_text(text, source, target):
    return GoogleTranslator(source=source, target=target).translate(text)

def detect_language(text):
    try:
        return detect(text)
    except:
        return "Unknown"
