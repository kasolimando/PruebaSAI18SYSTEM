from flask_sqlalchemy import SQLAlchemy
from Core.Database.ICompanyDBContext import ICompanyDBContext

class CompanyDBContext(ICompanyDBContext):

  def __init__(self,app):
    self.db = SQLAlchemy(app) 


  def getAll(self,model_cls):
    return self.db.session.query(model_cls).all()

  def getByField(self, model_cls, field, value):
    return self.db.session.query(model_cls).filter(getattr(model_cls, field) == value).first()


  def save(self,entity):
    self.db.session.add(entity)
    self.db.session.commit()
  
  def delete(self,entity):
    self.db.session.delete(entity)
    self.db.session.commit()

  def Commit(self):
    self.db.session.commit()
