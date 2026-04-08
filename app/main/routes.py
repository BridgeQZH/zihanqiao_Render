from flask import current_app, jsonify, render_template

from app.main import bp


@bp.get("/")
def home():
    featured_courses = [
        {
            "title": "Bridge Basics",
            "level": "Beginner",
            "description": "Build confidence with the rules, flow of play, and table etiquette.",
        },
        {
            "title": "Bidding Fundamentals",
            "level": "Intermediate",
            "description": "Understand common bidding ideas and communicate clearly with your partner.",
        },
        {
            "title": "Declarer Play",
            "level": "Intermediate",
            "description": "Practice planning a hand, managing trumps, and creating extra winners.",
        },
    ]

    return render_template("main/home.html", featured_courses=featured_courses)


@bp.get("/health")
def health():
    return jsonify({"status": "ok", "service": current_app.config["APP_NAME"]}), 200
