from flask import render_template, request
from app import app


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/login/", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return render_template("index.html")
    else:
        return "Method not post"


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def inter_error(e):
    return render_template("500.html"), 500


@app.route("/base")
def base():
    return render_template("base.html")
