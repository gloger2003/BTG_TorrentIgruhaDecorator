from enum import unique
from app import (db)


class Genre(db.Model):
    __tablename__ = 'Genres'
    id = db.Column(db.Integer(), primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False, unique=True)
    url = db.Column(db.String(500), nullable=False)


db.create_all()
db.session.commit()
