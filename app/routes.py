# app/routes.py

from app import app, request, render_template


@app.route('/', methods=['GET'])
@app.route('/home/', methods=['GET'])
@app.route('/index/', methods=['GET'])
def home_page():
    return render_template("homepage.html", url=request.host)


@app.route('/user/', methods=['GET'])
@app.route('/user/<name>', methods=['GET'])
def user_page(name="Invite"):
    return render_template("user.html", name=name)


@app.route('/about/', methods=['GET'])
def about_page():
    return render_template("about.html")


@app.route('/contact-us/', methods=['GET'])
def contact_page():
    return render_template("contact-us.html")