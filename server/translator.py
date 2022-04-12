from translate import Translator
from flask import Blueprint, request, Response

TRANSLATE = Blueprint("translate", __name__)

translate_route = "/translate"

@TRANSLATE.route(f"{translate_route}", methods=['GET'])
def translate():

    try:
        from_language,  = request.get_json()["from"], 
    except Exception as error:
        from_language = "fr"

    try:
        to_language = request.get_json()["to"]
    except Exception as error:
        to_language = "en"

    try:
        sentence = request.get_json()["sentence"]
    except Exception as error:
        return {"error": "'sentence' parameter is required.", "message": str(error)}, 404
    
    translator = Translator(to_lang=to_language, from_lang=from_language)

    translation = translator.translate(sentence)

    return {
        "base_sentence": sentence,
        "translation": translation
    }, 200