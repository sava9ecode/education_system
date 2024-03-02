# HardQode. The test task from HeadHunter.

A piece of an education project.

## Quick Start

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Docker

```bash
docker build -t education_project .
docker run --rm -d -p 8000:8000 education_project
```
