# app/routes.py

from flask import request, render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/', methods=['GET'])
@app.route('/home/', methods=['GET'])
@app.route('/index/', methods=['GET'])
def home_page():
    return render_template("homepage.html", url=request.host)


@app.route('/login/', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Connexion envoyée pour l\'utilisateur {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('home_page'))
    return render_template("login.html", form=form)


@app.route('/about/', methods=['GET'])
def about_page():
    return render_template("about.html")


@app.route('/contact-us/', methods=['GET'])
def contact_page():
    return render_template("contact-us.html")


@app.route('/user/', methods=['GET'])
@app.route('/user/<name>', methods=['GET'])
def user_page(name="Invite"):
    return render_template("user.html", name=name)
