from flask import Blueprint, render_template

bp = Blueprint('bp',__name__)

@bp.route("/")
def home():
    return "<h1>Hello, Flask!</h1>"

@bp.route("/login/<nome>")
def login(nome=None):
    return "<center><h1>Ola, "+nome+"! <br />Faca seu login!</h1></center>"

@bp.route("/auladeontem/")
def carrega():
    return render_template('aula2_ex1.html')
