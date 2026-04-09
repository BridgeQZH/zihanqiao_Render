from flask import current_app, jsonify, render_template

from app.main import bp


@bp.get("/")
def home():
    featured_courses = [
        {
            "title": "桥牌入门基础",
            "level": "初学者",
            "description": "从牌局流程、桌上礼仪到基本思路，先把入门框架搭起来。",
        },
        {
            "title": "叫牌核心概念",
            "level": "进阶",
            "description": "理解常见叫牌表达，学会和搭档稳定传递牌力与牌型信息。",
        },
        {
            "title": "定约打法训练",
            "level": "进阶",
            "description": "练习做庄计划、将牌管理和建立额外赢墩的基本方法。",
        },
    ]

    return render_template("main/home.html", featured_courses=featured_courses)


@bp.get("/health")
def health():
    return jsonify({"status": "ok", "service": current_app.config["APP_NAME"]}), 200
