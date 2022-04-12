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
    "sentence": "I am a computer science student, studying in the university of Lille."
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
            "type": "ADP",
            "word": "in"
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
    "base_text": "I am a computer scientist in Lille.",
    "elements": {
        "entities": [
            [
                "Lille",
                384
            ]
        ],
        "nouns": [
            "I",
            "a computer scientist",
            "Lille"
        ],
        "verbs": []
    }
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
            "suggestions": [
                "scientist"
            ],
            "type": "NOUN",
            "word": "scientis"
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
    "base_text": "I am a computer scientis in Lille.",
    "elements": {
        "entities": [
            [
                "Lille",
                384
            ]
        ],
        "nouns": [
            "I",
            "a computer scientis",
            "Lille"
        ],
        "verbs": []
    }
}
```