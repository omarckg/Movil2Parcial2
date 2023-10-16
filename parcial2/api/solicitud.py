from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.solicitud import Solicitud, SolicitudesSchema
from models.pasajero import Pasajero, PasajerosSchema

ruta_solicitud = Blueprint("ruta_solicitud",__name__)

solicitud_schema = SolicitudesSchema()
solicitudes_schema = SolicitudesSchema(many=True)

@ruta_solicitud.route('/solicitudes', methods=['GET'])
def solicitud():
    resultall = Solicitud.query.all() # Select * from Pasajeros
    resultado_solicitud = solicitudes_schema.dump(resultall)
    return jsonify(resultado_solicitud)

@ruta_solicitud.route('/savesolicitud', methods=['POST'])
def save():
    idpasajero = request.json['idpasajero']
    punto_origen = request.json['punto_origen']
    hora = request.json['hora']
    punto_final = request.json['punto_final']
    new_solicitud = Solicitud(
        idpasajero,
        punto_origen,
        hora,
        punto_final,
        
    )
    db.session.add(new_solicitud)
    db.session.commit()
    return "Datos guardados con éxito"


@ruta_solicitud.route('/updatesolicitud', methods=['PUT'])
def Update():
    id = request.json['id']
    idpasajero = request.json['idpasajero']
    punto_origen = request.json['punto_origen']
    Hora = request.json['hora']
    punto_final = request.json['punto_final']
    
    solicitud = Solicitud.query.get(id)
    if solicitud:
        print(solicitud)
        solicitud.idpasajero = idpasajero
        solicitud.punto_origen = punto_origen
        solicitud.Hora = Hora
        solicitud.punto_final = punto_final
        
        db.session.commit()
        return "Datos actualizados con éxito"
    else:
        return "Error"

@ruta_solicitud.route('/deletesolicitud/<id>', methods=['DELETE'])
def eliminar(id):
    solicitud = Solicitud.query.get(id)
    db.session.delete(solicitud)
    db.session.commit()
    return jsonify(
        solicitud_schema.dump(solicitud),
                   )