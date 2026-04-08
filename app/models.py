from __future__ import annotations

from app.extensions import db


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    slug = db.Column(db.String(150), unique=True, nullable=False, index=True)
    summary = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    sort_order = db.Column(db.Integer, nullable=False, default=0)
    is_published = db.Column(db.Boolean, nullable=False, default=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.now(), nullable=False)
    updated_at = db.Column(
        db.DateTime(timezone=True),
        server_default=db.func.now(),
        onupdate=db.func.now(),
        nullable=False,
    )

    modules = db.relationship(
        "Module",
        back_populates="course",
        order_by="Module.sort_order",
        cascade="all, delete-orphan",
        lazy="selectin",
    )

    @property
    def published_modules(self) -> list["Module"]:
        return [module for module in self.modules if module.published_lessons]

    @property
    def published_lesson_count(self) -> int:
        return sum(len(module.published_lessons) for module in self.modules)


class Module(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"), nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    slug = db.Column(db.String(150), unique=True, nullable=False, index=True)
    summary = db.Column(db.String(255), nullable=False)
    sort_order = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.now(), nullable=False)
    updated_at = db.Column(
        db.DateTime(timezone=True),
        server_default=db.func.now(),
        onupdate=db.func.now(),
        nullable=False,
    )

    course = db.relationship("Course", back_populates="modules")
    lessons = db.relationship(
        "Lesson",
        back_populates="module",
        order_by="Lesson.sort_order",
        cascade="all, delete-orphan",
        lazy="selectin",
    )

    @property
    def published_lessons(self) -> list["Lesson"]:
        return [lesson for lesson in self.lessons if lesson.is_published]


class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    module_id = db.Column(db.Integer, db.ForeignKey("module.id"), nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    slug = db.Column(db.String(150), unique=True, nullable=False, index=True)
    summary = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text, nullable=False)
    sort_order = db.Column(db.Integer, nullable=False, default=0)
    is_published = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.now(), nullable=False)
    updated_at = db.Column(
        db.DateTime(timezone=True),
        server_default=db.func.now(),
        onupdate=db.func.now(),
        nullable=False,
    )

    module = db.relationship("Module", back_populates="lessons")

    @property
    def course(self) -> Course:
        return self.module.course
