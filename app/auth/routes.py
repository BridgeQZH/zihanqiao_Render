from flask import render_template

from app.auth import bp


@bp.get("/")
def index():
    return render_template("auth/index.html")
