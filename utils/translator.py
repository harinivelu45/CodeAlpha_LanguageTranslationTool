
from deep_translator import GoogleTranslator
from langdetect import detect
from deep_translator.exceptions import TooManyRequests
import time

def translate_text(text, source, target):
    for attempt in range(2):
        try:
            return GoogleTranslator(
                source=source,
                target=target
            ).translate(text)
        except TooManyRequests:
            if attempt == 0:
                time.sleep(3)
            else:
                return None
        except Exception as e:
            print(f"Translation error: {e}")
            return None

def detect_language(text):
    try:
        return detect(text)
    except Exception:
        return "Unknown"
