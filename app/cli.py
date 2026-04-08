import click

from app.extensions import db
from app.seed import seed_sample_course


def register_commands(app) -> None:
    @app.cli.command("init-db")
    def init_db_command() -> None:
        """Create the database tables."""
        db.create_all()
        click.echo("Database tables created.")

    @app.cli.command("seed-sample-data")
    def seed_sample_data_command() -> None:
        """Seed the sample bridge course content."""
        db.create_all()
        course = seed_sample_course()
        click.echo(f"Sample data ready: {course.title}")
