from flask_cors import CORS
import spacy
from spellchecker import SpellChecker
from flask import Blueprint, request, Response

ANALYSE = Blueprint("analyse", __name__)
CORS(ANALYSE)

analyse_route = "/analyse"

nlp = spacy.load("en_core_web_sm")
spell = SpellChecker()

@ANALYSE.route(f"{analyse_route}", methods=['POST'])
def analyse():


    try:
        sentence: str = request.get_json()["sentence"]
    except Exception as error:
        return {"error": "'sentence' is a required parameter", "message": str(error)}, 404

    # Process whole documents
    text = (sentence)
    doc = nlp(text)

    analyses = [
        {
            "word": str(token),
            "type": str(token.pos_),
            "corrected": spell.correction(str(token)) if spell.correction(str(token)) != str(token) else None,
            "suggestions": [sugg for sugg in spell.candidates(str(token))][:-1]
        }
        for token in doc
    ]

    for element in analyses:
        if element["corrected"] is not None:
            text = text.replace(element["word"], element["corrected"])

    if text != sentence:
        doc = nlp(text)

    return {
        "base_text": sentence,
        "text_corrected": text if text != sentence else None,
        "analyses": analyses,
        "elements": {
            "nouns" : [chunk.text for chunk in doc.noun_chunks],
            "verbs": [token.lemma_ for token in doc if token.pos_ == "VERB"],
            "entities": [[entity.text, entity.label] for entity in doc.ents]
        }
    }