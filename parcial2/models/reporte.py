from config.db import  db, ma, app

class Reporte(db.Model):
    __tablename__ = "tblreporte"

    id = db.Column(db.Integer, primary_key=True)
    id_viaje = db.Column(db.Integer, db.ForeignKey('tblviaje.id'))
    id_pago = db.Column(db.Integer, db.ForeignKey('tblpago.id'))
    fecha = db.Column(db.String(50))

    def __init__(self, id_viaje, id_pago, fecha):
        self.id_viaje = id_viaje
        self.id_pago = id_pago
        self.fecha = fecha


with app.app_context():
    db.create_all()

class ReportesSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_viaje','id_pago', 'fecha')