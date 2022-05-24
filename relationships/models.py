from sqlalchemy.exc import SQLAlchemyError

from app import db


class Relationship(db.Model):
    __tablename__ = 'relacionamento'

    email = db.Column('email', db.String, primary_key=True)
    id_solides = db.Column('id_solides', db.String)
    id_ad = db.Column('id_ad', db.String)
    id_avaya = db.Column('id_avaya', db.String)

    def update(self, data):
        try:
            for key in data.keys():
                setattr(self, key, data.get(key, None))

            db.session.commit()
        except SQLAlchemyError:
            pass

    def __init__(self, data):
        for key in data.keys():
            if hasattr(self, key):
                setattr(self, key, data.get(key, None))
        db.session.add(self)
        db.session.commit()
