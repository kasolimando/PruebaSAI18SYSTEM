from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

base = declarative_base()

class Company(base):

    __tablename__ = 'company'
    compania = Column(Integer, primary_key=True)
    descripcion = Column(String(40), nullable=False)
    direccion1 = Column(String(40), nullable=False)
    direccion2 = Column(String(40), nullable=False)
    direccion3 = Column(String(40), nullable=False)
    telefono1 = Column(String(40), nullable=False)
    telefono2 = Column(String(40), nullable=False)
    telefono3 = Column(String(40), nullable=False)
    correo_electronico = Column(String(40),unique=True, nullable=False)
    pagina_web = Column(String(40), unique=True, nullable=False)

    def __repr__(self):
        return self.username

    def __init__(self,descripcion,direccion1,direccion2,direccion3,telefono1,telefono2,telefono3,correo_electronico,pagina_web):
        self.descripcion = descripcion
        self.direccion1 = direccion1
        self.direccion2 = direccion2
        self.direccion3 = direccion3
        self.telefono1 = telefono1
        self.telefono2 = telefono2
        self.telefono3 = telefono3
        self.correo_electronico = correo_electronico
        self.pagina_web = pagina_web