from flask import abort, render_template

from app.courses import bp
from app.extensions import db
from app.models import Course, Lesson


@bp.get("/courses")
@bp.get("/courses/")
def index():
    courses = db.session.scalars(
        db.select(Course)
        .where(Course.is_published.is_(True))
        .order_by(Course.sort_order.asc(), Course.title.asc())
    ).all()

    return render_template("courses/index.html", courses=courses)


@bp.get("/courses/<course_slug>")
def course_detail(course_slug: str):
    course = db.session.scalar(
        db.select(Course)
        .where(Course.slug == course_slug, Course.is_published.is_(True))
    )
    if course is None:
        abort(404)

    return render_template("courses/detail.html", course=course)


@bp.get("/lessons/<lesson_slug>")
def lesson_detail(lesson_slug: str):
    lesson = db.session.scalar(
        db.select(Lesson)
        .where(Lesson.slug == lesson_slug, Lesson.is_published.is_(True))
    )
    if lesson is None:
        abort(404)

    published_lessons = lesson.module.published_lessons
    current_index = next(
        (index for index, published_lesson in enumerate(published_lessons) if published_lesson.id == lesson.id),
        0,
    )
    next_lesson = published_lessons[current_index + 1] if current_index + 1 < len(published_lessons) else None

    return render_template(
        "courses/lesson_detail.html",
        lesson=lesson,
        module=lesson.module,
        course=lesson.course,
        next_lesson=next_lesson,
    )
