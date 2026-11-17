from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calories.db'
db = SQLAlchemy(app)

class FoodEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    food = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, default=datetime.now)

# Домашня сторінка
@app.route('/')
def index():
    return render_template('index.html')

# Сторінка калорій
@app.route('/calories')
def calories():
    entries = FoodEntry.query.order_by(FoodEntry.date.desc()).all()
    return render_template('calories.html', entries=entries)

# Додати їжу, потім повернутись на сторінку калорій
@app.route('/add', methods=['POST'])
def add():
    food = request.form.get('food')
    if food:
        db.session.add(FoodEntry(food=food))
        db.session.commit()
    return redirect(url_for('calories'))

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)