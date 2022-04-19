<h1 align="center">NLP API</h1>

This is the Learning English NLP API documentation.

## Routes

- ### [**GET**] '/translate'

**Body :**

```json
{
    "sentence": "Bonjour tout le monde."
}
```

**Result :**

```json
{
    "base_sentence": "Bonjour tout le monde.",
    "translation": "Hello everybody."
}
```

- ### [**GET**] '/analyse'

**Body :**

```json
{
    "sentence": "I am a computer scientist, and I am currently studying in the university of Lille."
}
```

**Result :**

```json
{
    "analyses": [
        {
            "corrected": null,
            "suggestions": [],
            "type": "PRON",
            "word": "I"
        },
        {
            "corrected": null,
            "suggestions": [],
            "type": "AUX",
            "word": "am"
        },
        {
            "corrected": null,
            "suggestions": [],
            "type": "DET",
            "word": "a"
        },
        {
            "corrected": null,
            "suggestions": [],
            "type": "NOUN",
            "word": "computer"
        },
        {
            "corrected": null,
            "suggestions": [],
            "type": "NOUN",
            "word": "scientist"
        },
        {
            "corrected": null,
            "suggestions": [],
            "type": "PUNCT",
            "word": ","
        },
        {
            "corrected": null,
            "suggestions": [],
            "type": "CCONJ",
            "word": "and"
        },
        {
            "corrected": null,
            "suggestions": [],
            "type": "PRON",
            "word": "I"
        },
        {
            "corrected": null,
            "suggestions": [],
            "type": "AUX",
            "word": "am"
        },
        {
            "corrected": null,
            "suggestions": [],
            "type": "ADV",
            "word": "currently"
        },
        {
            "corrected": null,
            "suggestions": [],
            "type": "VERB",
            "word": "studying"
        },
        {
            "corrected": null,
            "suggestions": [],
            "type": "ADP",
            "word": "in"
        },
        {
            "corrected": null,
            "suggestions": [],
            "type": "DET",
            "word": "the"
        },
        {
            "corrected": null,
            "suggestions": [],
            "type": "PROPN",
            "word": "university"
        },
        {
            "corrected": null,
            "suggestions": [],
            "type": "ADP",
            "word": "of"
        },
        {
            "corrected": null,
            "suggestions": [],
            "type": "PROPN",
            "word": "Lille"
        },
        {
            "corrected": null,
            "suggestions": [],
            "type": "PUNCT",
            "word": "."
        }
    ],
    "base_text": "I am a computer scientist, and I am currently studying in the university of Lille.",
    "elements": {
        "entities": [
            [
                "the university of Lille",
                383
            ]
        ],
        "nouns": [
            "I",
            "a computer scientist",
            "I",
            "the university",
            "Lille"
        ],
        "verbs": [
            "study"
        ]
    },
    "text_corrected": null
}
```

> If your sentence contains errors, the suggesed corrections will be placed in the result

```json
{
    "analyses": [
        {
            "corrected": null,
            "suggestions": [],
            "type": "PRON",
            "word": "I"
        },
        {
            "corrected": null,
            "suggestions": [],
            "type": "AUX",
            "word": "am"
        },
        {
            "corrected": null,
            "suggestions": [],
            "type": "DET",
            "word": "a"
        },
        {
            "corrected": null,
            "suggestions": [],
            "type": "NOUN",
            "word": "computer"
        },
        {
            "corrected": "scientist",
            "suggestions": [],
            "type": "NOUN",
            "word": "sientist"
        },
        {
            "corrected": null,
            "suggestions": [],
            "type": "PUNCT",
            "word": ","
        },
        {
            "corrected": null,
            "suggestions": [],
            "type": "CCONJ",
            "word": "and"
        },
        {
            "corrected": null,
            "suggestions": [],
            "type": "PRON",
            "word": "I"
        },
        {
            "corrected": null,
            "suggestions": [],
            "type": "AUX",
            "word": "am"
        },
        {
            "corrected": null,
            "suggestions": [],
            "type": "ADV",
            "word": "currently"
        },
        {
            "corrected": null,
            "suggestions": [],
            "type": "VERB",
            "word": "studying"
        },
        {
            "corrected": null,
            "suggestions": [],
            "type": "ADP",
            "word": "in"
        },
        {
            "corrected": null,
            "suggestions": [],
            "type": "DET",
            "word": "the"
        },
        {
            "corrected": "university",
            "suggestions": [],
            "type": "PROPN",
            "word": "Universty"
        },
        {
            "corrected": null,
            "suggestions": [],
            "type": "ADP",
            "word": "of"
        },
        {
            "corrected": null,
            "suggestions": [],
            "type": "PROPN",
            "word": "Lille"
        },
        {
            "corrected": null,
            "suggestions": [],
            "type": "PUNCT",
            "word": "."
        }
    ],
    "base_text": "I am a computer sientist, and I am currently studying in the Universty of Lille.",
    "elements": {
        "entities": [
            [
                "the university of Lille",
                383
            ]
        ],
        "nouns": [
            "I",
            "a computer scientist",
            "I",
            "the university",
            "Lille"
        ],
        "verbs": [
            "study"
        ]
    },
    "text_corrected": "I am a computer scientist, and I am currently studying in the university of Lille."
}
```