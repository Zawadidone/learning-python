# imports
from flask import Flask, render_template, request, session, flash, redirect, url_for
from functools import wraps
import MySQLdb as db

# configuration
DATABASE = "flask"
USERNAME = "admin"
PASSWORD = "admin"
SECRET_KEY = "hard_to_guess"

app = Flask(__name__)

# pulls in app configuration by looking for UPPERCASE variables
app.config.from_object(__name__)


# function used for connecting to database
def connect():
    conn = db.connect(host="localhost", user="root", password="asdf", db="flask")
    c = conn.cursor()
    return conn, c


def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if "logged_in" in session:  # if sessions exists login
            return test(*args, **kwargs)
        else:  # if not log in first
            flash("You need to log in first.")
            return redirect(url_for("login"))
    return wrap


@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    status_code = 200
    if request.method == "POST":
        if request.form["username"] != app.config["USERNAME"] or request.form["password"] != app.config["PASSWORD"]:
            error = "Invalid Credentials. Please try again."
            status_code = 401
        else:
            session["logged_in"] = True
            return redirect(url_for("main"))
    return render_template("login.html", error=error), status_code


@app.route("/main")
@login_required
def main():
    conn, c = connect()
    c.execute("SELECT * FROM flask.posts")
    posts = c.fetchall()
    conn.close()
    return render_template("main.html", posts=posts)


@app.route("/logout")
def logout():  # kill session
    session.pop("logged_in", None)
    flash("You were logged out")
    return redirect(url_for("login"))


@app.route("/add", methods=["POST"])
@login_required
def add():
    rpost = request.form["post"]
    rtitle = request.form["title"]
    if not rtitle or not rpost:
        flash("All fields are required. Please try again.")
        return redirect(url_for("main"))
    else:
        conn, c = connect()
        c.execute("""
        INSERT INTO flask.posts(title, post) 
        VALUES (%s, %s)""", (rtitle, rpost))
        conn.commit()
        conn.close()
        flash("New entry was successfly posted!")
        return redirect(url_for("main"))


if __name__ == "__main__":
    app.run(debug=True)
