from flask import Blueprint

app_blueprint = Blueprint('app_blueprint',__name__)

@app_blueprint.route("/")
def home():
    return "<h1>Hello, Flask</h1>"

@app_blueprint.route("/login/<nome>")
def login(nome=None):
    return "<center><h1>Ola, "+nome+"! <br />Faca seu login!</h1></center>"

