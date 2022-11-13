import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
    )
language_translator.set_service_url(url)

def english_french(english_text):
    """Function for translating English to French"""
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    result=json.dumps(translation, indent=2, ensure_ascii=False)  
    french_text=result[50:57]  
    return french_text

def french_english(french_text):
    """Function for translating English to French"""
    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    result=json.dumps(translation, indent=2, ensure_ascii=False)
    english_text=result[50:55]
    return english_text