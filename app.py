
import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌍",
    layout="centered"
)

st.title("🌍 Language Translation Tool")
st.write("Translate text into different languages.")

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

col1, col2 = st.columns(2)

with col1:
    source = st.selectbox(
        "Source Language",
        list(LANGUAGES.keys())
    )

with col2:
    target = st.selectbox(
        "Target Language",
        list(LANGUAGES.keys())[1:],
        index=1
    )

user_text = st.text_area(
    "Enter Text",
    placeholder="Type something here..."
)

if st.button("Translate", type="primary"):

    if not user_text.strip():
        st.warning("Please enter some text.")

    elif source == target:
        st.warning("Please select different languages.")

    else:
        try:
            translator = GoogleTranslator(
                source=LANGUAGES[source],
                target=LANGUAGES[target]
            )

            result = translator.translate(user_text)

            if result:
                st.subheader("Translated Text")
                st.success(result)
            else:
                st.error("No translation received.")

        except Exception as e:
            st.error(f"Translation Error: {e}")
            st.exception(e)

st.caption("CodeAlpha AI Internship Project")
