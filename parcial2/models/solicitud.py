from config.db import db, ma, app

class Solicitud(db.Model):
    __tablename__ = "tblsolicitud"

    id = db.Column(db.Integer, primary_key=True)
    idpasajero = db.Column(db.Integer, db.ForeignKey('tblpasajero.id'))
    punto_origen = db.Column(db.String(50))
    Hora = db.Column(db.String(50))
    punto_final = db.Column(db.String(50))

    def __init__(self,idpasajero, punto_origen, Hora, punto_final):
        self.idpasajero = idpasajero
        self.punto_origen = punto_origen
        self.Hora = Hora
        self.punto_final = punto_final

with app.app_context():
    db.create_all()

class SolicitudesSchema(ma.Schema):
    class Meta:
        fields = ('id','idpasajero', 'punto_origen', 'Hora','punto_final')