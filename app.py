import streamlit as st
import requests
from deep_translator import GoogleTranslator

st.set_page_config(page_title="Language Translation Tool")

LANGUAGES = {
    "Auto Detect": "auto",
    "English": "en",
    "Hindi": "hi",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Marathi": "mr",
    "Japanese": "ja"
}

st.title("🌐 Language Translation Tool")
st.write("Translate text into different languages.")

col1, col2 = st.columns(2)

with col1:
    source = st.selectbox("Source Language", list(LANGUAGES.keys()))

with col2:
    target = st.selectbox("Target Language", list(LANGUAGES.keys())[1:], index=1)

text = st.text_area("Enter Text")

if st.button("Translate"):
    if not text.strip():
        st.warning("Enter some text.")
    elif source == target:
        st.warning("Select different languages.")
    else:
        try:
            result = GoogleTranslator(
                source=LANGUAGES[source],
                target=LANGUAGES[target]
            ).translate(text)

            st.subheader("Translated Text")
            st.write(result)

        except Exception:
            st.error("Translation service unavailable. Try again.")

st.caption("CodeAlpha AI Internship Project")
