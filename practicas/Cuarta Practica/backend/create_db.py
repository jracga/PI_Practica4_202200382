from main import app
from db import db
from models.user import User

with app.app_context():
    db.create_all()
