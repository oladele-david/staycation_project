from datetime import datetime
from app.extensions import db


class Country(db.Model):
    """Country model for storing country related details """

    __tablename__ = 'countries'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    code = db.Column(db.String(8), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    states = db.relationship('State', backref='country', lazy=True)

    def __repr__(self):
        return "<Country '{}'>".format(self.name)
