from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    contraseña = db.Column(db.String(100), nullable=False)
    imagen = db.Column(db.String(100))
    plata = db.Column(db.Integer, default=50)  
    nombreciudad = db.Column(db.String(100))




class TiposEdificios(db.Model):
    __tablename__ = 'tiposedificios'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    imagen = db.Column(db.String(255))
    clase = db.Column(db.CHAR(1), nullable=False)
    poblacion = db.Column(db.Integer)
    precio = db.Column(db.Integer, nullable=False)
    descripcion = db.Column(db.Text)
    tiemporecaudacion = db.Column(db.Interval, nullable=False)
    platarecaudacion = db.Column(db.Integer)


class MisEdificios(db.Model):
    __tablename__ = 'misedificios'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255), nullable=False)
    imagen = db.Column(db.String(255), nullable=False)
    clase = db.Column(db.String(1), nullable=False)
    poblacion = db.Column(db.Integer, nullable=False)
    descripcion = db.Column(db.Text,nullable=False)
    tiemporecaudacion = db.Column(db.Interval, nullable=False)
    platarecaudacion = db.Column(db.Integer, nullable=False)
    idusuario = db.Column(db.Integer, ForeignKey('usuarios.id'), nullable=False)
    idtipoedificio = db.Column(db.Integer, ForeignKey('tiposedificios.id'), nullable=False)

    usuario = relationship('Usuario', back_populates='misedificios')
    tiposedificio = relationship('TiposEdificios', back_populates='misedificios')

Usuario.misedificios = relationship('MisEdificios', order_by=MisEdificios.id, back_populates='usuario')
TiposEdificios.misedificios = relationship('MisEdificios', order_by=MisEdificios.id, back_populates='tiposedificio')