from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date
from ai import estimate_nutrition

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calories.db'
db = SQLAlchemy(app)

class FoodEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    food = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, default=datetime.now)
    # Нові колонки: можуть бути порожніми, якщо AI не відповів
    calories = db.Column(db.Integer)
    protein = db.Column(db.Float)
    carbs = db.Column(db.Float)
    fat = db.Column(db.Float)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calories')
def calories():
    # Тільки записи за сьогодні
    today_start = datetime.combine(date.today(), datetime.min.time())
    entries = (FoodEntry.query
               .filter(FoodEntry.date >= today_start)
               .order_by(FoodEntry.date.desc())
               .all())

    # Сума за день (None рахуємо як 0)
    totals = {
        'calories': sum(e.calories or 0 for e in entries),
        'protein': sum(e.protein or 0 for e in entries),
        'carbs': sum(e.carbs or 0 for e in entries),
        'fat': sum(e.fat or 0 for e in entries),
    }
    return render_template('calories.html', entries=entries, totals=totals)

@app.route('/add', methods=['POST'])
def add():
    food = request.form.get('food')
    if food:
        nutrition = estimate_nutrition(food) or {}  # {} якщо AI повернув None
        entry = FoodEntry(
            food=food,
            calories=nutrition.get('calories'),
            protein=nutrition.get('protein'),
            carbs=nutrition.get('carbs'),
            fat=nutrition.get('fat'),
        )
        db.session.add(entry)
        db.session.commit()
    return redirect(url_for('calories'))

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)