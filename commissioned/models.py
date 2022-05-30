from sqlalchemy.exc import SQLAlchemyError

from app import db


class Commissioned(db.Model):
    __tablename__ = 'cgp_ccomiss'
    
    id = db.Column('codigo', db.String, primary_key=True)
    classification = db.Column('classe', db.String, nullable=False)
    level = db.Column('nivel', db.String)
    name = db.Column('nome', db.String, nullable=False)

    quantity = db.Column('quantidade', db.SmallInteger, nullable=False)
    unitary_value = db.Column('valorunitario', db.Float, nullable=False)

    nomef =  db.Column('nomef', db.String)
    nomem =  db.Column('nomem', db.String)
    cargoc =  db.Column('cargoc', db.String)

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
