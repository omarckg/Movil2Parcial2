from config.db import db, ma, app

class Viaje(db.Model):
    __tablename__ = "tblsolicitud"

    id = db.Column(db.Integer, primary_key=True)
    idpasajero = db.Column(db.Integer, db.ForeignKey('tblpasajero.id'))
    idvehiculo = db.Column(db.Integer, db.ForeignKey('tblvehiculos.id'))
    Hora_inicio = db.Column(db.String(50))
    Hora_fin = db.Column(db.String(50))
    trayecto = db.Column(db.String(50))

    def __init__(self,idpasajero, idvehiculo, hora_inicio, hora_fin, trayecto):
        self.idpasajero = idpasajero
        self.idvehiculo = idvehiculo
        self.Hora_inicio = hora_inicio
        self.Hora_fin = hora_fin
        self.trayecto = trayecto

with app.app_context():
    db.create_all()

class ViajesSchema(ma.Schema):
    class Meta:
        fields = ('id','idpasajero', 'idvehiculo', 'hora_inicio', 'hora_fin', 'trayecto')