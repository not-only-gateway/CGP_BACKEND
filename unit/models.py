from sqlalchemy.exc import SQLAlchemyError

from app import db


class Unit(db.Model):
    __tablename__ = 'cgp_unidade'

    acronym = db.Column('sigla', db.String, primary_key=True, nullable=False)
    name = db.Column('nome', db.String, nullable=False)
    parent_unit = db.Column('subordinacao', db.String, db.ForeignKey('cgp_unidade.sigla', ondelete='CASCADE'))
    root = db.Column('raiz', db.String, db.ForeignKey('cgp_unidade.sigla', ondelete='CASCADE'), nullable=False)

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
