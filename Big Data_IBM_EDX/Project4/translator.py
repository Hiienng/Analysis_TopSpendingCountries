#pip install ibm_watson wget
# Import the necessary library for translation
import ibm_watson
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def translate_to_french(text):
    url_lt='https://api.us-south.language-translator.watson.cloud.ibm.com/instances/a7ca5d1d-7b0a-412d-bbd6-f7b78512bbc1'
    apikey_lt='K-NmJvjRJhNyMfCm1WPlWu7IBzRgF3U7AAoXsPeFFAk_'
    version_lt='2018-05-01'

    # Set up authentication and instantiate the Language Translator service
    authenticator = IAMAuthenticator(apikey_lt)
    language_translator = ibm_watson.LanguageTranslatorV3(
        version=version_lt,
        authenticator=authenticator)
    language_translator.set_service_url(url_lt)

    # Translate the text from English to French
    response = language_translator.translate(
        text=text,
        source='en',
        target='fr'
    ).get_result()

    # Extract and return the translated text
    translation = response['translations'][0]['translation']
    return translation