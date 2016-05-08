from flask import render_template, request, flash, session, redirect, url_for
from app import app
import config
from dbconnect import connection

app.secret_key = config.secret_key
c, conn = connection()

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
        session['logged_in'] = True
        return render_template("index.html")
    else:
        flash("login unsuccessful")
        return render_template("login.html")


@app.route("/register/", methods=['GET','POST'])
def register():
    if request.method == 'POST':
        flash("login successful")

        return render_template("index.html")
    else:
        flash("login unsuccessful")
        return render_template('register.html')


@app.route("/logout/")
def logout():
    # session.pop('logged_in')
    return redirect(url_for('index'))


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
    return render_template("contact.html")


@app.route("/about/")
def about():
    return render_template("about.html")
