from flask import Flask, render_template, request, redirect, url_for, flash
import hashlib
import json
import os

app = Flask(__name__)
app.secret_key = "secret-key-demo"

USERS_FILE = "users.json"


def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=4)


def hash_password(password):
    # UTF-8 encoding allows emoji passwords
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def register_user(username, password):
    users = load_users()

    if username in users:
        return False, "Username already exists."

    users[username] = hash_password(password)
    save_users(users)
    return True, "User registered successfully."


def login_user(username, password):
    users = load_users()

    if username not in users:
        return False, "Username not found."

    if users[username] == hash_password(password):
        return True, "Login successful."
    else:
        return False, "Incorrect password."


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        success, message = register_user(username, password)
        flash(message)

        if success:
            return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        success, message = login_user(username, password)
        flash(message)

    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)