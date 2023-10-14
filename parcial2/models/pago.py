from config.db import db, ma, app

class Pago(db.Model):
    __tablename__ = "tblpago"

    id = db.Column(db.Integer, primary_key=True)
    idpasajero = db.Column(db.Integer, db.ForeignKey('tblpasajero.id'))
    fecha = db.Column(db.String(50))
    monto = db.Column(db.String(50))
    metodo_pago = db.Column(db.String(50))

    def __init__(self,idpasajero, fecha, monto, metodo_pago):
        self.idpasajero = idpasajero
        self.fecha = fecha
        self.monto = monto
        self.metodo_pago = metodo_pago

with app.app_context():
    db.create_all()

class PagosSchema(ma.Schema):
    class Meta:
        fields = ('id','idpasajero', 'fecha', 'monto','metodo_pago')