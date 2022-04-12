import spacy
from flask import Blueprint, request, Response

ANALYSE = Blueprint("analyse", __name__)

analyse_route = "/analyse"

@ANALYSE.route(f"{analyse_route}", methods=['GET'])
def analyse():

    nlp = spacy.load("en_core_web_sm")

    try:
        sentence = request.get_json()["sentence"]
    except Exception as error:
        return {"error": "'sentence' is a required parameter", "message": str(error)}, 404

    # Process whole documents
    text = (sentence)
    doc = nlp(text)

    return {
        "base_text": sentence,
        "analyses": [(str(token), str(token.pos_)) for token in doc],
        "elements": {
            "nouns" : [chunk.text for chunk in doc.noun_chunks],
            "verbs": [token.lemma_ for token in doc if token.pos_ == "VERB"],
            "entities": [[entity.text, entity.label] for entity in doc.ents]
        }
    }