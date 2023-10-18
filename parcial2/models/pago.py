from config.db import db, ma, app

class Pago(db.Model):
    __tablename__ = "tblpago"

    id = db.Column(db.Integer, primary_key=True)
    idviaje = db.Column(db.Integer, db.ForeignKey('tblviaje.id'))
    fecha = db.Column(db.String(50))
    monto = db.Column(db.String(50))
    metodo_pago = db.Column(db.String(50))

    def __init__(self,idviaje, fecha, monto, metodo_pago):
        self.idviaje = idviaje
        self.fecha = fecha
        self.monto = monto
        self.metodo_pago = metodo_pago

with app.app_context():
    db.create_all()

class PagosSchema(ma.Schema):
    class Meta:
        fields = ('id','idviaje', 'fecha', 'monto','metodo_pago')