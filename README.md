# Health Tracker

A web app for tracking calories and daily activity, with AI-powered food analysis (in progress).

## Current Features (v0.1.0)
- Home page with navigation between features
- Log food entries with timestamps
- Entries stored in a SQLite database

## Planned
- AI calorie estimation from text descriptions
- Food recognition from photos
- Step, weight and height tracking
- Dashboard with charts and AI analysis

## Tech Stack
- Python, Flask
- Flask-SQLAlchemy (SQLite)
- HTML, CSS, Jinja2

## Running Locally
```bash
git clone https://github.com/sviat-z/Project-1.git
cd Project-1
python3 -m venv venv
source venv/bin/activate
pip install flask flask-sqlalchemy
python3 app.py
```
Then open http://127.0.0.1:5000
