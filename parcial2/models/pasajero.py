from config.db import db, ma, app

class Pasajero(db.Model):
    __tablename__ = "tblpasajero"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    telefono = db.Column(db.String(50))
    ubicacion = db.Column(db.String(50))

    def __init__(self, nombre, telefono, ubicacion):
        
        self.nombre = nombre
        self.telefono = telefono
        self.ubicacion = ubicacion

with app.app_context():
    db.create_all()

class PasajerosSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'telefono','ubicacion')