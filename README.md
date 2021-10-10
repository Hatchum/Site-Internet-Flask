# SITE-INTERNET-FLASK

## Configuration de l'environnement 'env'
python3 -m venv env

## Installation des dépendances pour l'environnement 'env'
1. pip install Flask  
2. pip install python-dotenv  
3. pip install flask-wtf  
4. pip install flask-sqlalchemy  
5. pip install flask-migrate  
6. pip install psycopg2

## Activation de l'environnement 'env'
env\Scripts\activate

## Configuration des variables d'environnement pour le lancement du server
(Ces variables sont présentes dans le fichier .flaskenv)
* set FLASK_APP=app  
* set FLASK_ENV=development

## Execution du server
* flask run  
* flask run --host=0.0.0.0 --port=XXXX

## URL d'acces
http://127.0.0.1:5000/