import uuid

from sqlalchemy.exc import SQLAlchemyError
import os
from app import db, app


class Collaborator(db.Model):
    __tablename__ = 'cgp_colaborador'

    id = db.Column('codigo', db.String, primary_key=True)

    image = db.Column('imagem_caminho', db.String)
    registration = db.Column('matricula', db.String)
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

    linkage = db.Column('vinculo', db.String, db.ForeignKey('cgp_vinculo.codigo', ondelete='SET NULL'))
    effective = db.Column('cefetivo', db.String, db.ForeignKey('cgp_cefetivo.codigo', ondelete='SET NULL'))
    commissioned = db.Column('ccomiss', db.String, db.ForeignKey('cgp_ccomiss.codigo', ondelete='SET NULL'))
    unit = db.Column('unidade', db.String, db.ForeignKey('cgp_unidade.sigla', ondelete='SET NULL'))
    marital_status = db.Column('estcivil', db.String, db.ForeignKey('cgp_estcivil.codigo', ondelete='SET NULL'))
    instruction = db.Column('instruc', db.String, db.ForeignKey('cgp_instruc.codigo', ondelete='SET NULL'))
    solides_id = db.Column('solides_id', db.BigInteger)


    def update(self, data):
        try:
            for key in data.keys():
                if key == 'image':
                    if self.image is not None:
                        try:
                            os.remove(self.image)
                        except OSError:
                            pass

                    if data[key] is not None and len(data[key]) > 0:
                        try:
                            path = app.config.get('MEDIA', '') + str(uuid.uuid4()) + '.txt'
                            print(path, len(str(data[key])))
                            f = open(path, "a")
                            f.write(str(data[key]))
                            f.close()
                            setattr(self, key, path)
                        except Exception as e:
                            print(e)
                    else:
                        setattr(self, key, None)
                elif hasattr(self, key):
                    setattr(self, key, data.get(key, None))
            db.session.commit()
        except SQLAlchemyError:
            pass

    def __init__(self, data):
        for key in data.keys():
            if key == 'image':
                path = app.config.get('MEDIA', '') + str(uuid.uuid4()) + '.txt'
                f = open(path, "a")
                f.write(data.get(key, ''))
                f.close()
                setattr(self, key, path)
            elif hasattr(self, key):
                setattr(self, key, data.get(key, None))
        db.session.add(self)
        db.session.commit()
