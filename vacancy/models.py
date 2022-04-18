from sqlalchemy.exc import SQLAlchemyError

from app import db


class Vacancy(db.Model):
    __tablename__ = 'cgp_distribccomiss'

    id = db.Column('codigo', db.String, primary_key=True)

    commissioned = db.Column('ccomiss', db.String, db.ForeignKey('cgp_ccomiss.codigo', ondelete='CASCADE'), nullable=False)
    unit = db.Column('unidade', db.String, db.ForeignKey('cgp_unidade.sigla', ondelete='SET NULL'))
    holder = db.Column('titular', db.String, db.ForeignKey('cgp_colaborador.codigo', ondelete='SET NULL'))
    substitute = db.Column('substituto', db.String, db.ForeignKey('cgp_colaborador.codigo', ondelete='SET NULL'))


    nomef =  db.Column('nomef', db.String, nullable=False)
    nomem =  db.Column('nomem', db.String, nullable=False)
    cargoc =  db.Column('cargoc', db.String, nullable=False)

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
