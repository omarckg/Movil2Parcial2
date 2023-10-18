from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.pago import Pago, PagosSchema
from models.viajes import Viaje, ViajesSchema

ruta_pago = Blueprint("ruta_pago",__name__)

pago_schema = PagosSchema()
Pagos_schema = PagosSchema(many=True)

@ruta_pago.route('/pagos', methods=['GET'])
def pago():
    resultall = Pago.query.all() # Select * from Pasajeros
    resultado_pago = Pagos_schema.dump(resultall)
    return jsonify(resultado_pago)

@ruta_pago.route('/savepago', methods=['POST'])
def save():
    idviaje = request.json['idviaje']
    fecha = request.json['fecha']
    monto = request.json['monto']
    metodo_pago = request.json['metodo_pago']
    new_pago = Pago(
        idviaje,
        fecha,
        monto,
        metodo_pago,
        
    )
    db.session.add(new_pago)
    db.session.commit()
    return "Datos guardados con éxito"

@ruta_pago.route('/Relacionpago', methods=['POST'])
def dostabla():
    datos = {}
    resultado = db.session.query(Viaje,Pago). \
        select_from(Viaje).join(Pago).all()
    i=0
    for viaje, pago in resultado:
        i+=1
        datos[i]={
            'viaje':viaje.id,
            'pago': pago.idpasajero, 
        }
    return datos

@ruta_pago.route('/updatepago', methods=['PUT'])
def Update():
    id = request.json['id']
    idviaje = request.json['idviaje']
    fecha = request.json['fecha']
    monto = request.json['monto']
    metodo_pago = request.json['metodo_pago']
    
    pago = Pago.query.get(id)
    if pago:
        print(pago)
        pago.idviaje = idviaje
        pago.fecha = fecha
        pago.monto = monto
        pago.metodo_pago = metodo_pago
        
        db.session.commit()
        return "Datos actualizados con éxito"
    else:
        return "Error"

@ruta_pago.route('/deletepago/<id>', methods=['DELETE'])
def eliminar(id):
    pago = Pago.query.get(id)
    db.session.delete(pago_schema)
    db.session.commit()
    return jsonify(
        pago_schema.dump(pago),
                   )