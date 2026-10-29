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

if "history" not in st.session_state:
    st.session_state.history = []

col1, col2 = st.columns(2)

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
        src = "auto" if source == "Auto Detect" else languages[source]

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
                st.warning(
                    "Speech generation is unavailable right now."
                )

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