# PROJECT 4 - AI - TEXT TO SPEECH 

This is a part of the AI project from IBM course which give:
- The requirement for Clean Code
- API code
- AI Project to transfer from text to speech and then translate from eng to spanish  

## Part 1: Translation part
### 1. Standard
for terminal: pip install ibm_watson wget

    import json
    from ibm_watson import LanguageTranslatorV3
    from ibm_cloud_sdk_core.authenticators import IAMAuthenticator    

    #Add the url and api key in IBM
    url_lt=''
    apikey_lt=''
    version_lt='2018-05-01'

    #Create language translator object
    authenticator = IAMAuthenticator(apikey_lt)
    language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
    language_translator.set_service_url(url_lt)
    language_translator

    #Get a Lists the languages that the service can identify
    from pandas import json_normalize

    json_normalize(language_translator.list_identifiable_languages().get_result(), "languages")

    #Using method **translate** to translate the text
    translation_response = language_translator.translate(\
        text=recognized_text, model_id='en-es')

    #Showing the dictionary
    translation=translation_response.get_result()
    
    #Get word into sentence
    spanish_translation =translation['translations'][0]['translation']
### 2. Another approach

    # Import the necessary library for translation
    import json
    import ibm_watson
    from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

    def english_to_french(text):
        # Set up authentication and instantiate the Language Translator service
        authenticator = IAMAuthenticator('<YOUR_API_KEY>')
        language_translator = ibm_watson.LanguageTranslatorV3(
            version='<YOUR_VERSION>',
            authenticator=authenticator
        )
        language_translator.set_service_url('<YOUR_URL>')

        # Translate the text from English to French
        response = language_translator.translate(
            text=text,
            source='en',
            target='fr'
        ).get_result()

        # Extract and return the translated text
        translation = response['translations'][0]['translation']
        return translation




## Part 2: Text to speech
