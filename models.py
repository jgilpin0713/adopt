from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def connect_db(app):
    """ Connect to database"""
    db.app = app
    db.init_app(app)

DEFAULT_URL = "https://www.ucsf.edu/sites/default/files/styles/full_bleed__image/public/2020-11/astonishing-animals-komodo-dragon.jpg"

class Pet(db.Model):
    """ Pets for Adoption"""
    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(20), nullable = False)
    species = db.Column(db.String(30), nullable = False)
    photo_url = db.Column(db.Text, default = DEFAULT_URL)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable = False, default = True)


