from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    contraseña = db.Column(db.String(100), nullable=False)
    imagen = db.Column(db.String(100))
    plata = db.Column(db.Integer, default=0)  




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

