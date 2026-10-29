
from deep_translator import GoogleTranslator
from deep_translator.exceptions import TooManyRequests
from langdetect import detect
import time


def translate_text(text, source, target):
    if not text or not text.strip():
        return None

    for attempt in range(2):
        try:
            translator = GoogleTranslator(
                source=source,
                target=target
            )

            result = translator.translate(text)
            return result

        except TooManyRequests:
            if attempt == 0:
                time.sleep(3)
            else:
                print("Translation service rate limit reached.")
                return None

        except Exception as error:
            print(f"Translation error: {error}")
            return None

    return None


def detect_language(text):
    try:
        return detect(text)
    except Exception:
        return "Unknown"
