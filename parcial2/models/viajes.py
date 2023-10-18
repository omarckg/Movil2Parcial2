from config.db import db, ma, app

class Viaje(db.Model):
    __tablename__ = "tblviaje"

    id = db.Column(db.Integer, primary_key=True)
    idsolicitud = db.Column(db.Integer, db.ForeignKey('tblsolicitud.id'))
    idvehiculo = db.Column(db.Integer, db.ForeignKey('tblvehiculo.id'))
    Hora_inicio = db.Column(db.String(50))
    Hora_fin = db.Column(db.String(50))
    trayecto = db.Column(db.String(50))

    def __init__(self,idsolicitud, idvehiculo, hora_inicio, hora_fin, trayecto):
        self.idsolicitud = idsolicitud
        self.idvehiculo = idvehiculo
        self.Hora_inicio = hora_inicio
        self.Hora_fin = hora_fin
        self.trayecto = trayecto

with app.app_context():
    db.create_all()

class ViajesSchema(ma.Schema):
    class Meta:
        fields = ('id','idsolicitud', 'idvehiculo', 'hora_inicio', 'hora_fin', 'trayecto')