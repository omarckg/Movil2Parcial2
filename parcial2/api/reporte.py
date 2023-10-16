from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.reporte import Reporte, ReportesSchema
from models.viajes import Viaje, ViajesSchema
from models.pago import Pago, PagosSchema


ruta_Reporte = Blueprint("ruta_Reporte", __name__)

Reporte_schema =ReportesSchema()
Reportes_schema = ReportesSchema(many=True)

@ruta_Reporte.route('/Reportes', methods=['GET'])
def reporte():
    resultall = Reporte.query.all() #Select * from Clientes
    resultado_Reporte= Reportes_schema.dump(resultall)
    return jsonify(resultado_Reporte)

@ruta_Reporte.route("/saveReporte", methods=["POST"])
def save():
    idviaje = request.json["idviaje"]
    idpago = request.json["idpago"]
    fecha = request.json["fecha"]
    new_Reporte = Reporte(
        idviaje,
        idpago,
         fecha,
    )
    db.session.add(new_Reporte)
    db.session.commit()
    return "datos guardado con exito"

@ruta_Reporte.route('/RelacionReporte', methods=['POST'])
def dostabla():
    datos = {}
    resultado = db.session.query(Viaje,Pago,Reporte). \
        select_from(Viaje).join(Reporte).all()
    i=0
    for viaje, pago, reporte  in resultado:
        i+=1
        datos[i]={
            'pasajero':viaje.id,
            'vehiculo': pago.id, 
        }
    return datos

@ruta_Reporte.route("/updateReporte", methods=["PUT"])
def Update():
    id = request.json["id"]
    idviaje = request.json["idviaje"]
    idpago= request.json["idpago"]
    fecha = request.json["fecha"]
    reporte= Reporte.query.get(id)
    if reporte:
        print(reporte)
        reporte.idviaje = idviaje
        reporte.idpago = idpago
        reporte.fecha = fecha
        db.session.commit()
        return "Datos actualizado con exitos"
    else:
        return "Error"
    
@ruta_Reporte.route("/deleteReporte/<id>", methods=["DELETE"])
def eliminar(id):
    reporte = Reporte.query.get(id)
    db.session.delete(reporte)
    db.session.commit()
    return jsonify(
       Reporte_schema.dump( reporte),
    )