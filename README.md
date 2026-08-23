# MediCare Hospital Management System

Django Class-Based Views + SQLite + responsive UI.

Features: Dashboard, Patient CRUD/search/filter, Doctor CRUD/search/filter,
Appointment CRUD/search/filter, Django admin, responsive UI, Render-ready deployment.

Local:
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Render is configured by render.yaml.

SQLite is intentional. Render's default filesystem is ephemeral, so database data
can be lost after a restart/redeploy. Permanent production data requires a
persistent disk or managed database.
