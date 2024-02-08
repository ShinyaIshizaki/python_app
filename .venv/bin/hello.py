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

@app.route("/user/<username>")
def user_profile(username):
  return f"User {escape(username)}"

@app.route("/post/<int:post_id>")
def show_post(post_id):
  return f"Post {escape(post_id)}"

@app.route("/path/<path:sub_path>")
def show_subpath(sub_path):
  return f"Subpath {escape(sub_path)}"

@app.route("/projects/")
def projects():
  return "The project page"

@app.route("/about")
def about():
  return "The about page"