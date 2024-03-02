# HardQode. The test task from HeadHunter.

A piece of an education project.

## Quick Start

```bash
mkdir education_project && cd education_project
git clone git@github.com:sava9ecode/education_system.git .
python -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
cat .env_sample > .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Docker

```bash
docker build -t education_project .
docker run --rm -d -p 8000:8000 education_project
```
