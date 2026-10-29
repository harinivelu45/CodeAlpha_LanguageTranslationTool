
import requests
from langdetect import detect, LangDetectException

def detect_language(text):
    try:
        return detect(text)
    except LangDetectException:
        return "Unknown"

def translate_text(text, source, target):
    if not text or not text.strip():
        return None

    try:
        if source.lower() == "auto":
            source = detect_language(text)

        if source == "Unknown":
            return None

        # Split text into chunks of at most 450 characters
        chunks = [
            text[i:i + 450]
            for i in range(0, len(text), 450)
        ]
        translated_chunks = []

        for chunk in chunks:
            response = requests.get(
                "https://api.mymemory.translated.net/get",
                params={
                    "q": chunk,
                    "langpair": f"{source}|{target}"
                },
                timeout=20
            )
            response.raise_for_status()
            data = response.json()

            if data.get("responseStatus") != 200:
                print("Translation API error:", data.get("responseDetails"))
                return None

            translated_chunks.append(
                data["responseData"]["translatedText"]
            )

        return " ".join(translated_chunks)

    except Exception as error:
        print("Translation error:", error)
        return None
