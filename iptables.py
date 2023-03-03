# save this as app.py
from flask import Flask, render_template, redirect, url_for, request, flash

app = Flask(__name__)


@app.route("/")
def start():
    return render_template ("index.html")

@app.route("/alias")
def alias():
    return render_template ("Alias.html")

@app.route("/nat_filter")
def nat_filter():
    return render_template ("nat.html")
