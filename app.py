import streamlit as st
from deep_translator import GoogleTranslator
from deep_translator.exceptions import LanguageNotSupportedException

st.set_page_config(page_title="Language Translation Tool", page_icon="🌐", layout="centered")

LANGUAGES = {
    "Auto Detect": "auto",
    "English": "en",
    "Hindi": "hi",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Japanese": "ja",
    "Chinese (Simplified)": "zh-CN",
    "Arabic": "ar",
    "Bengali": "bn",
    "Marathi": "mr",
    "Tamil": "ta",
    "Telugu": "te",
    "Urdu": "ur",
    "Portuguese": "pt",
    "Russian": "ru",
    "Korean": "ko",
    "Italian": "it",
}

st.title("🌐 Language Translation Tool")
st.write("Translate text between different languages in a few seconds.")

left, right = st.columns(2)
with left:
    source_name = st.selectbox("Source language", list(LANGUAGES.keys()), index=0)
with right:
    target_name = st.selectbox("Target language", [x for x in LANGUAGES if x != "Auto Detect"], index=1)

text = st.text_area("Enter text", height=160, placeholder="Type or paste your text here...")

if st.button("Translate", type="primary", use_container_width=True):
    if not text.strip():
        st.warning("Please enter some text first.")
    else:
        try:
            translator = GoogleTranslator(
                source=LANGUAGES[source_name],
                target=LANGUAGES[target_name]
            )
            translated = translator.translate(text.strip())
            st.subheader("Translated text")
            st.text_area("Result", value=translated or "", height=160)
            if translated:
                st.download_button(
                    "Download translation",
                    data=translated,
                    file_name="translation.txt",
                    mime="text/plain",
                    use_container_width=True
                )
        except Exception as error:
            st.error(f"Translation failed. Check your internet connection and try again. Details: {error}")

st.caption("Built for the CodeAlpha Artificial Intelligence Internship.")
