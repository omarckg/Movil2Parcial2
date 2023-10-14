from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.viajes import Viaje, ViajesSchema

ruta_Viaje = Blueprint("ruta_Viaje", __name__)

Viaje_schema =ViajesSchema()
Viajes_schema = ViajesSchema(many=True)

@ruta_Viaje.route('/Viajes', methods=['GET'])
def viaje():
    resultall = Viaje.query.all() #Select * from Clientes
    resultado_Viaje= Viajes_schema.dump(resultall)
    return jsonify(resultado_Viaje)

@ruta_Viaje.route("/saveViaje", methods=["POST"])
def save():
    idpasajero = request.json['idpasajero']
    idvehiculo = request.json['idvehiculo']
    hora_inicio = request.json[" hora_inicio"]
    Hora_fin= request.json[" hora_fin"]
    trayecto = request.json[" trayecto"]
    new_viaje= viaje(
        idpasajero,
        idvehiculo,
        hora_inicio,
        Hora_fin,
        trayecto,
    )
    db.session.add(new_viaje)
    db.session.commit()
    return "datos guardado con exito"

@ruta_Viaje.route("/updateViaje", methods=["PUT"])
def Update():
    id = request.json["id"]
    idpasajero = request.json['idpasajero']
    idvehiculo = request.json['idvehiculo']
    hora_inicio = request.json[" hora_inicio"]
    hora_fin= request.json[" hora_fin"]
    trayecto = request.json[" trayecto"]
    viaje= Viaje.query.get(id)
    if viaje:
        print(viaje)
        viaje.idpasajero = idpasajero
        viaje.idvehiculo = idvehiculo
        viaje.hora_inicio = hora_inicio
        viaje.hora_fin = hora_fin
        viaje.trayecto = trayecto
        db.session.commit()
        return "Datos actualizado con exitos"
    else:
        return "Error"
    
@ruta_Viaje.route("/deleteReporte/<id>", methods=["DELETE"])
def eliminar(id):
    viaje = Viaje.query.get(id)
    db.session.delete(viaje)
    db.session.commit()
    return jsonify(
       Viaje_schema.dump(viaje),
    )