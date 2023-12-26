# Language Translator App

This Streamlit web app translates text from *English* language to *German* language using the *Pre-trained OpenNMT-py models*.

#### Overview

The Language Translator App is a simple tool built using *Streamlit* and the *Pre-trained OpenNMT-py models*. It allows users to input word or sentences in a English language and translates them into German language.

#### Features

- Translate text or sentences from English language to German language.
- Uses OpenNMT-py pretrained model with ctranslate2.
- Displays translated text(s).

#### Installation

To run this app locally, follow these steps:

1. Clone this repository:

   ```bash
   git clone https://github.com/your_username/streamlit_translator.git
   cd streamlit_translator
   ```

2. `pip install -r requirements.txt`

#### Usage
 1. Run the app:
    ```bash
    streamlit run translator_nmt.py
    ```
2. Enter the word or sentences you want to translate.
3. Click on the "Translate" button to get the translated text.


#### Downloading the Pretrained Model

- Download the pretrained model from the following link:
  - [Transformer EN-DE WMT OpenONMT-py](https://s3.amazonaws.com/opennmt-models/transformer-ende-wmt-pyOnmt.tar.gz)
 - The pretrained model directory will contain two file:
    - `averaged-10-epoch.pt`
    - `sentencepiece.model`
 - For more information through the turorials provided in the reporsitory.

#### Convert the Model using CTranslate2

- Install CTranslate2 from the official repository available at:
  - [CTranslate2 GitHub Repository](https://github.com/OpenNMT/CTranslate2)
- Follow the instructions provided in the repository to install and set up CTranslate2.

#### Support
 - For any inquiries or support, please open an issue or contact [tungondugi@gmail.com](gmail.com)
