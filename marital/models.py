from sqlalchemy.exc import SQLAlchemyError

from app import db


class MaritalStatus(db.Model):
    __tablename__ = 'cgp_estcivil'

    id = db.Column('codigo', db.String, primary_key=True)
    description = db.Column('descricao', db.String,  nullable=False)


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
