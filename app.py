from flask import Flask
from flask import render_template
from flask import request, redirect

app = Flask(__name__)


@app.route("/")
def hello_world():
    return """
    Hello, World! 
    <a href="/about">Go to About Page</a>
    """


@app.route("/about")
def about():
    return """
    This is the about page
    <a href="/">Go to main</a>
    """


@app.route("/user/<username>")
def show_user_profile(username):
    return f"User {username}"


@app.route("/hello/<name>")
def hello(name):
    return render_template("hello.html", name=name)


@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    return redirect(f"/hello/{name}")


if __name__ == "__main__":
    app.run(debug=True)
