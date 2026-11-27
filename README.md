# Health Tracker

A web app for tracking calories and daily activity, with AI-powered nutrition analysis.

## Current Features (v0.2.0)
- Home page with navigation between features
- Log food entries in plain text (e.g. "2 eggs and toast")
- AI estimates calories, protein, carbs and fat for each entry (Google Gemini API)
- Daily totals on the calories page
- Entries stored in a SQLite database

## Planned
- Food recognition from photos
- Step, weight and height tracking
- Dashboard with charts and AI analysis

## Tech Stack
- Python, Flask
- Flask-SQLAlchemy (SQLite)
- Google Gemini API (`google-genai`)
- HTML, CSS, Jinja2

## Running Locally
```bash
git clone https://github.com/sviat-z/Project-1.git
cd Project-1
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file in the project root with your Gemini API key (free from [Google AI Studio](https://aistudio.google.com)):
```
GEMINI_API_KEY=your_key_here
```

Run the app:
```bash
python3 app.py
```
Then open http://127.0.0.1:5000

## Notes
- Nutrition values are AI estimates and may not be exact.
- If the AI is unavailable, entries are still saved without nutrition data.