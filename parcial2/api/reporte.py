from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.reporte import Reporte, ReportesSchema

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
    placa = request.json[" placa"]
    estado = request.json[" estado"]
    capacidad = request.json[" capacidades"]
    new_Reporte = Reporte(
        placa,
        estado,
        capacidad,
    )
    db.session.add(new_Reporte)
    db.session.commit()
    return "datos guardado con exito"

@ruta_Reporte.route("/updateReporte", methods=["PUT"])
def Update():
    id = request.json["id"]
    placa = request.json["id_aerolinea"]
    estado= request.json["modelo_avion"]
    capacidad = request.json["capacidad"]
    reporte= Reporte.query.get(id)
    if reporte:
        print(reporte)
        reporte.placa = placa
        reporte.estado = estado
        reporte.capacidad = capacidad
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