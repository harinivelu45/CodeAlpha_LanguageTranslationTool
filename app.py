import streamlit as st
from utils.translator import translate_text, detect_language
from utils.speech import text_to_speech

st.set_page_config(page_title="AI Language Translator", layout="wide")

st.title("🌍 AI Language Translation Tool")

languages = {
    "English":"en","Tamil":"ta","Hindi":"hi","French":"fr","German":"de",
    "Spanish":"es","Japanese":"ja","Chinese":"zh-CN","Arabic":"ar"
}

if "history" not in st.session_state:
    st.session_state.history = []

col1, col2 = st.columns(2)

with col1:
    source = st.selectbox("Source Language", ["Auto Detect"] + list(languages.keys()))
with col2:
    target = st.selectbox("Target Language", list(languages.keys()), index=1)

text = st.text_area("Enter Text", height=200)

if st.button("Translate"):
    if text.strip():
        src = "auto" if source == "Auto Detect" else languages[source]
        translated = translate_text(text, src, languages[target])
        detected = detect_language(text)

        st.subheader("Translated Text")
        st.success(translated)

        st.write(f"Detected Language: {detected}")
        st.write(f"Characters: {len(text)}")
        st.write(f"Words: {len(text.split())}")

        audio_file = text_to_speech(translated)
        with open(audio_file, "rb") as f:
            st.download_button("🔊 Download Speech", f, file_name="translation.mp3")

        st.download_button("📄 Download Text", translated, file_name="translation.txt")

        st.session_state.history.append(
            {"input": text, "output": translated}
        )

st.sidebar.title("Translation History")
for item in reversed(st.session_state.history[-10:]):
    st.sidebar.write("Input:", item["input"][:50])
    st.sidebar.write("Output:", item["output"][:50])
    st.sidebar.divider()
