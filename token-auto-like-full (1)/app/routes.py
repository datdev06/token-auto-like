from flask import render_template, request, redirect, session
import json, os

def routes(app):
    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/admin", methods=["GET", "POST"])
    def admin():
        if request.method == "POST":
            password = request.form.get("password")
            if password == "admin123":
                session["admin"] = True
                return redirect("/dashboard")
        return render_template("admin_login.html")

    @app.route("/dashboard")
    def dashboard():
        if not session.get("admin"):
            return redirect("/admin")
        return render_template("dashboard.html")