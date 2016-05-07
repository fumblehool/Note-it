from flask import render_template, request, flash, session
from app import app
import config

app.secret_key = config.secret_key
c, conn = config.connection()

@app.route("/")
def index():
    if "logged_in" not in session:
        return render_template("index.html")
    else:
        return render_template("dashboard.html")


@app.route("/login/", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        flash("login successful")
        return render_template("index.html")
    else:
        flash("login unsuccessful")
        return render_template("login.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def inter_error(e):
    return render_template("500.html"), 500


@app.route("/base")
def base():
    return render_template("base.html")


@app.route("/contact/")
def contact():
    return "Contact page"


@app.route("/about")
def about():
    return "About page"
