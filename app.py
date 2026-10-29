<<<<<<< HEAD

import streamlit as st
from utils.translator import translate_text, detect_language
from utils.speech import text_to_speech

st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 AI Language Translation Tool")
st.write("Translate text into different languages.")

languages = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Chinese": "zh-CN",
    "Arabic": "ar"
}
=======

from deep_translator import GoogleTranslator
from deep_translator.exceptions import TooManyRequests
from langdetect import detect
import time


def translate_text(text, source, target):
    if not text or not text.strip():
        return None
>>>>>>> 1392c7f1d1200b6beba1ea1dbd271924d5db8fa3

    for attempt in range(2):
        try:
            translator = GoogleTranslator(
                source=source,
                target=target
            )

            result = translator.translate(text)
            return result

<<<<<<< HEAD
with col1:
    source = st.selectbox(
        "Source Language",
        ["Auto Detect"] + list(languages.keys())
    )

with col2:
    target = st.selectbox(
        "Target Language",
        list(languages.keys()),
        index=1
    )

text = st.text_area(
    "Enter Text",
    height=200,
    placeholder="Enter text to translate..."
)

if st.button("🌐 Translate", type="primary"):
    if not text.strip():
        st.warning("Please enter text to translate.")

    elif source != "Auto Detect" and source == target:
        st.warning("Choose different source and target languages.")

    else:
        src = (
            "auto"
            if source == "Auto Detect"
            else languages[source]
        )

        with st.spinner("Translating..."):
            translated = translate_text(
                text,
                src,
                languages[target]
            )

        if not translated:
            st.error(
                "Translation service is temporarily unavailable. "
                "Please wait and try again later."
            )

        else:
            st.subheader("Translated Text")
            st.text_area(
                "Translation Result",
                value=translated,
                height=150
            )

            detected = detect_language(text)

            st.write(f"Detected Language: {detected}")
            st.write(f"Characters: {len(text)}")
            st.write(f"Words: {len(text.split())}")

            st.download_button(
                "📄 Download Text",
                data=translated,
                file_name="translation.txt",
                mime="text/plain"
            )

            try:
                audio_file = text_to_speech(translated)

                with open(audio_file, "rb") as audio:
                    st.download_button(
                        "🔊 Download Speech",
                        data=audio.read(),
                        file_name="translation.mp3",
                        mime="audio/mpeg"
                    )

            except Exception:
                st.warning("Speech generation is unavailable right now.")

            st.session_state.history.append({
                "input": text,
                "output": translated
            })

st.sidebar.title("📝 Translation History")

if st.sidebar.button("Clear History"):
    st.session_state.history = []
    st.rerun()

for item in reversed(st.session_state.history[-10:]):
    st.sidebar.write("Input:", item["input"][:50])
    st.sidebar.write("Output:", item["output"][:50])
    st.sidebar.divider()
=======
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
>>>>>>> 1392c7f1d1200b6beba1ea1dbd271924d5db8fa3
