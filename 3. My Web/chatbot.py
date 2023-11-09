import streamlit as st
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# # Function to calculate age
# def calculate_age(year_of_birth):
#     current_year = 2023
#     age = current_year - year_of_birth
#     return age

#authen
api = 'UxKY7N5Iu1iITs77_lpTEBCuyJi_BsVNMk3mAbeFCbUf'
url = 'https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/1ac79c78-843b-403a-ba1c-8ecb1d0ba8b6'
ver = '2018-05-01'

authenticator = IAMAuthenticator(api)
lt = LanguageTranslatorV3(version = ver, authenticator = authenticator)
lt.set_service_url(url)

def translate_tool(ini_text):
    #ini_text = str(input("We will help to translate English-Japanese. Please input your sentences here: "))
    tran_text  = lt.translate(text = ini_text, model_id='en-ja').get_result()
    Showed_text = tran_text['translations'][0]['translation']
    return Showed_text