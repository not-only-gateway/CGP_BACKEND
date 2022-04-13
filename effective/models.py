from sqlalchemy.exc import SQLAlchemyError

from app import db


class Effective(db.Model):
    __tablename__ = 'cgp_cefetivo'

    id = db.Column('codigo', db.String, primary_key=True)

    name = db.Column('nome', db.String, nullable=False)
    regime = db.Column('regime', db.String)


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
