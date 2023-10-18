from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.pasajero import Pasajero, PasajerosSchema


ruta_pasajeros = Blueprint("ruta_pasajero",__name__)

pasajero_schema = PasajerosSchema()
pasajeros_schema = PasajerosSchema(many=True)

@ruta_pasajeros.route('/pasajeros', methods=['GET'])
def pasajero():
    resultall = Pasajero.query.all() # Select * from Pasajeros
    resultado_pasajero = pasajeros_schema.dump(resultall)
    return jsonify(resultado_pasajero)

@ruta_pasajeros.route('/savepasajero', methods=['POST'])
def save():
    
    nombre = request.json['nombre']
    telefono = request.json['telefono']
    ubicacion = request.json['direccion']
    new_pasajero = Pasajero(
        
        nombre,
        telefono,
        ubicacion,
        
    )
    db.session.add(new_pasajero)
    db.session.commit()
    return "Datos guardados con éxito"



@ruta_pasajeros.route('/updatepasajero', methods=['PUT'])
def Update():
    id = request.json['id']
    
    nombre = request.json['nombre']
    telefono = request.json['telefono']
    ubicacion = request.json['direccion']
    
    pasajero = Pasajero.query.get(id)
    if pasajero:
        print(pasajero)
        
        pasajero.nombre = nombre
        pasajero.telefono = telefono
        pasajero.ubicacion = ubicacion
        
        db.session.commit()
        return "Datos actualizados con éxito"
    else:
        return "Error"

@ruta_pasajeros.route('/deletepasajero/<id>', methods=['DELETE'])
def eliminar(id):
    pasajero = Pasajero.query.get(id)
    db.session.delete(pasajero)
    db.session.commit()
    return jsonify(
        pasajero_schema.dump(pasajero),
                   )