from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    due_date = db.Column(db.String(20))
    priority = db.Column(db.String(20), default="Média")
    done = db.Column(db.Boolean, default=False)
    image = db.Column(db.String(200), default="task.png")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
