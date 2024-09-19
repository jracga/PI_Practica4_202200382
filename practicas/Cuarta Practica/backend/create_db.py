#creación de tablas de la base de datos
from main import app
from db import db
from models.user import User
from models.publication import Publication, Comment     

with app.app_context():
    db.create_all()
