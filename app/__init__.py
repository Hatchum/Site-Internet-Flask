# app/__init__.py

from flask import Flask, request, render_template
# import socket


# our sexy awsome fucking website creation entry function
def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home_page():
        return render_template("homepage.html", url=request.host)

    @app.route('/user/')
    @app.route('/user/<name>')
    def user_page(name="Invite"):
        return render_template("user.html", name=name)

    @app.route('/about/')
    def about_page():
        return render_template("about.html")

    @app.route('/contact-us/')
    def contact_page():
        return render_template("contact-us.html")

    return app
