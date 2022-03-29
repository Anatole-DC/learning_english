from flask import Flask

API = Flask(__name__)

@API.get("/")
def homepage():
    return "Hello World !"

def main():
    API.run()

if __name__ == "__main__":
    main()
