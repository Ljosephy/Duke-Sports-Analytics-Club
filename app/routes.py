from flask import render_template, request, url_for
from app import app

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template("home.html")

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template("about.html")

@app.route('/profiles', methods=['GET', 'POST'])
def profiles():
    return render_template("profiles.html")

@app.route('/projects', methods=['GET', 'POST'])
def projects():
    return render_template("projects.html")

@app.route('/tutorial_post', methods=['GET', 'POST'])
def tutorial_post():
    return render_template("tutorial_post.html")