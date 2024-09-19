from db import db
from datetime import datetime

class Publication(db.Model):
    __tablename__ = 'publication'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    course_or_professor = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('publications', lazy=True))
    comments = db.relationship('Comment', backref='comment_list', lazy=True)


class Comment(db.Model):
    __tablename__ = 'comment'
    
    id = db.Column(db.Integer, primary_key=True)
    publication_id = db.Column(db.Integer, db.ForeignKey('publication.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    message = db.Column(db.Text, nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('comments', lazy=True))
    publication = db.relationship('Publication', backref='publication_comments', lazy=True)

