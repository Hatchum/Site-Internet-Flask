# app/__init__.py

from flask import Flask, request, render_template

app = Flask(__name__)
app.config["DEBUG"] = True

from app import routes
