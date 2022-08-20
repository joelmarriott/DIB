from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask('DIB')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dib.db'
db = SQLAlchemy(app)

class Display(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    street1 = db.Column(db.String(200), nullable=False)
    street2 = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    postcode = db.Column(db.String(8), nullable=False)     
    latitude = db.Column(db.String(8), nullable=False)     
    longitude = db.Column(db.String(8), nullable=False)     
    method = db.Column(db.String(200), nullable=False)
    photos = db.Column(db.String(200), nullable=False)
    link = db.Column(db.String(200), nullable=False)
    type = db.Column(db.String(20), nullable=False)
    info = db.Column(db.String(1000), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Display %r>'%self.id
        