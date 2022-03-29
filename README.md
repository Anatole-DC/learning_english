<h1 align="center">🇬🇧 Learning English 🇬🇧</h1>

_<h4 align="center">"It was mandatory, but it's still cool..."</h4>_

This is a repository made for teaching english sentences's structure, based on the Spacy python module.

This repository comes with two part, the [frontend](frontend) application, and the [backend](backend) server.

___


**Author**: Anatole de Chauveron, Adrien Bassail, Henri Boulnois, Tristan Six, Astrid Djouhassi Djoumessi

**Technos :** VueJS, Flask, Spacy

**Licence :** General Public Licence

___

## Summary

### [Frontend](frontend)

### [Server](server)

## Getting started

### Requirements

In order to use the application you will need the following requirements :

```bash
❯ python3 --version
Python 3.8.10

❯ virtualenv --version
virtualenv 20.0.17

❯ vue --version
@vue/cli 5.0.4

❯ yarn --version
1.22.18
```

### Installation

To install the project use the following command in the folder in which you want to store the application code :

```bash
git clone https://github.com/Anatole-DC/learning_english.git
```

You will then need to add a virtual environment to the [server](server) folder. To do that, inside the server folder, run :

```bash
❯ virtualenv <your-venv-name>
```

Finally install all the dependencies with :

```bash
source <your-venv-name>/bin/activate
pip install -r requirements.txt
```

### Running the project

**All instances :**

In order to run all instances at once, run :

```bash
❯ ./start.sh
```

**Only the API :**

In order to run the API, go to the [server](server) folder of the project and run :

```bash
python main.py
```

> Make sure you have your virtual environment configured and activated, otherwise you'll run into an error.

**Only the frontend (useless) :**

In order to run the frontend, place yourself in the [frontend](frontend/) folder of the project and run :

```bash
yarn serve
```

> This will be useless however, because the frontend is linked to the backend.

## Getting further

_For further informations about this repository, please contact us at **adechauveron@gmail.com**._