# Bridge Learning Flask Skeleton

Minimal, production-ready Flask starter for a bridge bidding learning website.

## Features

- Flask application factory pattern
- Blueprint structure for `main`, `auth`, and `courses`
- SQLAlchemy models for `Course`, `Module`, and `Lesson`
- Homepage route at `/`
- Health check at `/health`
- Public course routes at `/courses`, `/courses/<course_slug>`, and `/lessons/<lesson_slug>`
- Jinja templates with a shared `base.html`
- Sample seeded course content for bridge bidding fundamentals
- Static CSS for a modern educational experience
- Environment-driven configuration
- `wsgi.py` entrypoint for local runs and deployment

## Project Structure

```text
.
|-- app/
|   |-- __init__.py
|   |-- cli.py
|   |-- extensions.py
|   |-- models.py
|   |-- auth/
|   |-- courses/
|   |-- main/
|   |-- static/
|   `-- templates/
|-- config.py
|-- requirements.txt
`-- wsgi.py
```

## Local Run

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set environment variables.

PowerShell:

```powershell
$env:FLASK_CONFIG="development"
$env:SECRET_KEY="dev-secret-key"
$env:DATABASE_URL="sqlite:///bridge_learning.db"
```

macOS/Linux:

```bash
export FLASK_CONFIG=development
export SECRET_KEY=dev-secret-key
export DATABASE_URL=sqlite:///bridge_learning.db
```

4. Initialize the database and seed the sample course:

```bash
flask --app wsgi.py init-db
flask --app wsgi.py seed-sample-data
```

5. Start the app:

```bash
python wsgi.py
```

6. Open `http://127.0.0.1:5000`

## Environment Variables

- `FLASK_CONFIG`: `development` or `production`
- `SECRET_KEY`: Flask secret key
- `APP_NAME`: Optional site name override
- `DATABASE_URL`: PostgreSQL connection string for Render or a local SQLite URL
- `PORT`: Optional port for `wsgi.py`

## Deployment Note

For Render or another WSGI host, use:

```bash
gunicorn wsgi:app
```

On Render, point `DATABASE_URL` at your PostgreSQL instance, then run:

```bash
flask --app wsgi.py init-db
flask --app wsgi.py seed-sample-data
```
