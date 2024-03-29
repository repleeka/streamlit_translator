import nltk
import ctranslate2
import sentencepiece as spm
import streamlit as st


# Set the background color using set_page_config
st.set_page_config(
    page_title="Translator App",
    page_icon=":fast_forward:",
    layout="centered",  # Optional
)


def translate(source, translator, sp_source_model, sp_target_model):
    """Use CTranslate model to translate a sentence

    Args:
        source (str): Source sentences to translate
        translator (object): Object of Translator, with the CTranslate2 model
        sp_source_model (object): Object of SentencePieceProcessor, with the SentencePiece source model
        sp_target_model (object): Object of SentencePieceProcessor, with the SentencePiece target model
    Returns:
        Translation of the source text
    """

    source_sentences = nltk.sent_tokenize(source)
    source_tokenized = sp_source_model.encode(source_sentences, out_type=str)
    translations = translator.translate_batch(source_tokenized)
    translations = [translation[0]["tokens"] for translation in translations]
    translations_detokenized = sp_target_model.decode(translations)
    translation = " ".join(translations_detokenized)

    return translation


# [Modify] File paths here to the CTranslate2 SentencePiece models.
ct_model_path = "ende_ct2"
sp_source_model_path = "models/sentencepiece.model"
sp_target_model_path = "models/sentencepiece.model"

# Create objects of CTranslate2 Translator and SentencePieceProcessor to load the models
translator = ctranslate2.Translator(
    ct_model_path, "cpu")    # or "cuda" for GPU
sp_source_model = spm.SentencePieceProcessor(sp_source_model_path)
sp_target_model = spm.SentencePieceProcessor(sp_target_model_path)
#  ---------------------------------------------------------------------------------------------------------


# setting the color of the text in the page
text_color = "black"

st.title(":{}[:shinto_shrine: English to German]".format(text_color))
st.header(":{}[Language Translator]".format(text_color))

text_value = st.text_area(
    label=":{}[English Language]".format(text_color),
    placeholder="Enter word or sentences to translate.",
    max_chars=100,
    help=":{}[Enter only selected language sentences or words]".format(
        text_color),
)

if st.button("Translate"):
    if not text_value:
        st.warning("Enter Text")
    else:
        translated_text = translate(
            text_value, translator, sp_source_model, sp_source_model)
        st.text_area(
            label=":{}[German language]".format(
                text_color),
            placeholder="Translated texts will appear here.",
            disabled=True,
            value=translated_text,
        )
