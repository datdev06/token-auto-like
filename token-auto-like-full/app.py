from flask import Flask, render_template, request, redirect, session
from config import ADMIN_USERNAME, ADMIN_PASSWORD
import random, time

app = Flask(__name__)
app.secret_key = "supersecretkey"

def get_tokens():
    with open("tokens.txt") as f:
        return [line.strip() for line in f if line.strip()]

def save_log(uid):
    with open("log_uid.txt", "a") as f:
        f.write(f"{uid} - {time.strftime('%Y-%m-%d %H:%M:%S')}
")

@app.route("/", methods=["GET", "POST"])
def index():
    msg = ""
    if request.method == "POST":
        uid = request.form.get("uid")
        tokens = get_tokens()
        if tokens:
            token = random.choice(tokens)
            # Giả lập gọi API like
            print(f"Đã like UID {uid} bằng token {token}")
            save_log(uid)
            msg = f"✅ Đã like UID {uid}"
        else:
            msg = "❌ Hết token!"
    return render_template("index.html", message=msg)

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if not session.get("logged_in"):
        return redirect("/login")
    with open("tokens.txt") as f:
        tokens = [line.strip() for line in f]
    with open("log_uid.txt", "r") as f:
        logs = f.readlines()
    return render_template("admin.html", tokens=tokens, logs=logs)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if (request.form["username"] == ADMIN_USERNAME and
            request.form["password"] == ADMIN_PASSWORD):
            session["logged_in"] = True
            return redirect("/admin")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    return redirect("/")

if __name__ == "__main__":
    app.run()