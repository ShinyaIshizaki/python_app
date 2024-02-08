from flask import Flask
from markupsafe import escape

app = Flask(__name__)
# name = "User"

@app.route("/")
def index():
  return "Index Page"

@app.route("/hello")
def hello():
  return "Hello, world!"