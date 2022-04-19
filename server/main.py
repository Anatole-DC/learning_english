from flask import Flask

from translator import TRANSLATE
from analyses import ANALYSE

API = Flask(__name__)
API.register_blueprint(TRANSLATE)
API.register_blueprint(ANALYSE)

@API.get("/")
def homepage():
    return {
        "welcome": "Welcome to the NLP API, by FGES",
        "description": "See the documentation at /docs in order to start using the API."
    }

def main():
    API.run(
        host="0.0.0.0",
        port=5001
    )

if __name__ == "__main__":
    main()
