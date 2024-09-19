# config.py
import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db' # Ejemplo para SQLite
    SQLALCHEMY_TRACK_MODIFICATIONS = False
