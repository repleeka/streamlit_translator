import streamlit as st
from googletrans import Translator, LANGUAGES, LANGCODES

# Set the background color using set_page_config
st.set_page_config(
    page_title="Translator App",
    page_icon=":fast_forward:",
    layout="centered",  # Optional
)
translator = Translator()
langs = LANGUAGES
langCodes = LANGCODES


# setting the color of the text in the page
text_color = "black"

st.title(":{}[:shinto_shrine: Welcome]".format(text_color))
st.header(":{}[Language Translator]".format(text_color))

src_option = st.selectbox("Selected input language", [(v.capitalize()) for k,v in langs.items()])
text_value = st.text_area(
    label=":{}[{} Language]".format(text_color, src_option),
    placeholder="Enter text or sentences to translate.",
    max_chars=100,
    help=":{}[Enter only selected language sentences or words]".format(text_color),
)

dest_option = st.selectbox("Output language", [(v.capitalize()) for k,v in langs.items()])
if st.button("Translate"):
    if not text_value:  
        st.warning("Enter Text")
    else:
        translated_text = translator.translate(text=text_value, src=src_option, dest=dest_option)
        pronunciation = translated_text.pronunciation

        if not pronunciation:
            st.text_area(
            label=":{}[{} language]".format(text_color, dest_option.capitalize()),
            placeholder="Translated texts will appear here.",
            disabled=True,
            value=translated_text.text,
            )
        else:
            st.text_area(
            label=":{}[{} language]".format(text_color, dest_option.capitalize()),
            placeholder="Translated texts will appear here.",
            disabled=True,
            value=translated_text.text+"\n"+pronunciation,
            )