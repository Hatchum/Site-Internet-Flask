# SITE-INTERNET-FLASK :

## Configuration de l'environnement env
python3 -m venv env  

## Installation des dépendances
pip install Flask  
pip install python-dotenv  
pip install flask-wtf

## Activation de l'environnement env
env\Scripts\activate  

## Configuration des variables d'environnement pour le lancement du server (Ces variables sont présentes dans le fichier .flaskenv)
set FLASK_APP=app  
set FLASK_ENV=development

## Execution du server
flask run  
flask run --host=0.0.0.0

## URL d'acces
http://127.0.0.1:5000/