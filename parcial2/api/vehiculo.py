from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.vehiculo import Vehiculo, VehiculosSchema

ruta_Vehiculo = Blueprint("ruta_Vehiculo", __name__)

Vehiculo_schema = VehiculosSchema()
Vehiculos_schema = VehiculosSchema(many=True)

@ruta_Vehiculo.route('/Vehiculos', methods=['GET'])
def vehiculo():
    resultall = Vehiculo.query.all() #Select * from Clientes
    resultado_Vehiculo= Vehiculos_schema.dump(resultall)
    return jsonify(resultado_Vehiculo)

@ruta_Vehiculo.route("/saveVehiculo", methods=["POST"])
def save():
    placa = request.json[" placa"]
    estado = request.json[" estado"]
    capacidad = request.json[" capacidades"]
    new_Vehiculo = Vehiculo(
        placa,
        estado,
        capacidad,
    )
    db.session.add(new_Vehiculo)
    db.session.commit()
    return "datos guardado con exito"

@ruta_Vehiculo.route("/updateVehiculo", methods=["PUT"])
def Update():
    id = request.json["id"]
    placa = request.json["id_aerolinea"]
    estado= request.json["modelo_avion"]
    capacidad = request.json["capacidad"]
    vehiculo= Vehiculo.query.get(id)
    if vehiculo:
        print(vehiculo)
        vehiculo.placa = placa
        vehiculo.estado = estado
        vehiculo.capacidad = capacidad
        db.session.commit()
        return "Datos actualizado con exitos"
    else:
        return "Error"
    
@ruta_Vehiculo.route("/deleteVehiculo/<id>", methods=["GET"])
def eliminar(id):
    vehiculo = Vehiculo.query.get(id)
    db.session.delete(vehiculo)
    db.session.commit()
    return jsonify(
       Vehiculo_schema.dump(vehiculo),
    )