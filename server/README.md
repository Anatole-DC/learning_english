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
        [
            "I",
            "PRON"
        ],
        [
            "am",
            "AUX"
        ],
        [
            "a",
            "DET"
        ],
        [
            "computer",
            "NOUN"
        ],
        [
            "science",
            "NOUN"
        ],
        [
            "student",
            "NOUN"
        ],
        [
            ",",
            "PUNCT"
        ],
        [
            "studying",
            "VERB"
        ],
        [
            "in",
            "ADP"
        ],
        [
            "the",
            "DET"
        ],
        [
            "university",
            "PROPN"
        ],
        [
            "of",
            "ADP"
        ],
        [
            "Lille",
            "PROPN"
        ],
        [
            ".",
            "PUNCT"
        ]
    ],
    "base_text": "I am a computer science student, studying in the university of Lille.",
    "elements": {
        "entities": [
            [
                "the university of Lille",
                383
            ]
        ],
        "nouns": [
            "I",
            "a computer science student",
            "the university",
            "Lille"
        ],
        "verbs": [
            "study"
        ]
    }
}
```