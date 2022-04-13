from sqlalchemy.exc import SQLAlchemyError

from app import db


class Collaborator(db.Model):
    __tablename__ = 'cgp_colaborador'

    id = db.Column('codigo', db.String, primary_key=True)
    registration = db.Column('matricula', db.String, nullable=False)
    name = db.Column('nome', db.String, nullable=False)
    superior = db.Column('superior', db.String)
    birth = db.Column('nascimento', db.DateTime)
    gender = db.Column('genero', db.String, nullable=False)
    nationality = db.Column('nacionalidade', db.String, nullable=False)
    pne = db.Column('pne', db.String)
    admission = db.Column('admissao', db.DateTime)
    resignation = db.Column('demissao', db.DateTime)
    extension = db.Column('ramal', db.SmallInteger)
    personal_email = db.Column('emailpessoal', db.String)
    email = db.Column('email', db.String)
    degree = db.Column('grauh', db.String)

    linkage = db.Column('vinculo', db.String, db.ForeignKey('cgp_vinculo.codigo', ondelete='NO ACTION'))
    effective = db.Column('cefetivo', db.String, db.ForeignKey('cgp_cefetivo.codigo', ondelete='NO ACTION'))
    commissioned = db.Column('ccomiss', db.String, db.ForeignKey('cgp_ccomiss.codigo', ondelete='NO ACTION'))
    unit = db.Column('unidade', db.String, db.ForeignKey('cgp_unidade.sigla', ondelete='NO ACTION'))
    marital_status = db.Column('estcivil', db.String, db.ForeignKey('cgp_estcivil.codigo', ondelete='NO ACTION'))
    instruction = db.Column('instruc', db.String, db.ForeignKey('cgp_instruc.codigo', ondelete='NO ACTION'))



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
