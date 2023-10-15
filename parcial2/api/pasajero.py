from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.pasajero import Pasajero, PasajerosSchema
from models.vehiculo import Vehiculo, VehiculosSchema

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
    idvehiculo = request.json['idvehiculo']
    nombre = request.json['nombre']
    telefono = request.json['telefono']
    ubicacion = request.json['direccion']
    new_pasajero = Pasajero(
        idvehiculo,
        nombre,
        telefono,
        ubicacion,
        
    )
    db.session.add(new_pasajero)
    db.session.commit()
    return "Datos guardados con éxito"

@ruta_pasajeros.route('/Relacionpasajero', methods=['POST'])
def dostabla():
    datos = {}
    resultado = db.session.query(Vehiculo,Pasajero). \
        select_from(Vehiculo).join(Pasajero).all()
    i=0
    for vehiculo, pasajero in resultado:
        i+=1
        datos[i]={
            'vehiculo':vehiculo.id,
            'pasajero': pasajero.idvehiculo, 
        }
    return datos

@ruta_pasajeros.route('/updatepasajero', methods=['PUT'])
def Update():
    id = request.json['id']
    idvehiculo = request.json['idvehiculo']
    nombre = request.json['nombre']
    telefono = request.json['telefono']
    ubicacion = request.json['direccion']
    
    pasajero = Pasajero.query.get(id)
    if pasajero:
        print(pasajero)
        pasajero.idvehiculo = idvehiculo
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