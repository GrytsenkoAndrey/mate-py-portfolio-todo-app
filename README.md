# mate-py-portfolio-todo-app

A simple TODO list web application built with Django and Bootstrap 5.

## Features

- **Tasks**: create, update and delete tasks. Each task has:
  - content (description),
  - creation date (set automatically),
  - optional deadline,
  - completion status (`Done` / `Not done`),
  - any number of tags.
- **Complete / Undo**: toggle a task's status with one click.
- **Tags**: create, rename and delete tags on a separate page.
- Tasks are listed with undone tasks first, then ordered by deadline.
  Lists are paginated (10 items per page).

## Pages

| URL                       | Description           |
|---------------------------|-----------------------|
| `/`                       | Task list (home page) |
| `/tasks/create/`          | Add a task            |
| `/tasks/<id>/update/`     | Update a task         |
| `/tasks/<id>/delete/`     | Delete a task         |
| `/tasks/<id>/toggle/`     | Complete / undo task  |
| `/tags/`                  | Tag list              |
| `/tags/create/`           | Add a tag             |
| `/tags/<id>/update/`      | Update a tag          |
| `/tags/<id>/delete/`      | Delete a tag          |
| `/admin/`                 | Django admin          |

## Tech stack

- Python 3.14
- Django 6.1
- SQLite
- Bootstrap 5, django-crispy-forms (crispy-bootstrap5)
- django-debug-toolbar, whitenoise, python-dotenv
- flake8 (with flake8-quotes, pep8-naming) for linting

## Run locally

### 1. Clone the repository

```bash
git clone <repository-url>
cd mate-py-portfolio-todo-app
```

### 2. Create a virtual environment and install dependencies

With `pip`:

```bash
python3.14 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Or with [uv](https://docs.astral.sh/uv/):

```bash
uv venv --python 3.14
source .venv/bin/activate        # Windows: .venv\Scripts\activate
uv pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in the project root (next to `manage.py`):

```dotenv
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
```

You can generate a secret key with:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. (Optional) Create an admin user

```bash
python manage.py createsuperuser
```

### 6. Start the development server

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Tests and linting

```bash
python manage.py test todo
flake8 todo/ mate_py_portfolio_todo_app/
```
