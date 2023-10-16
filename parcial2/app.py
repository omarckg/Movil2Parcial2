from flask import Flask, jsonify,json
from config.db import  db, ma, app
from api.pasajero import Pasajero, ruta_pasajeros
from api.vehiculo import Vehiculo, ruta_Vehiculo
from api.viajes import Viaje, ruta_Viaje
from api.solicitud import Solicitud, ruta_solicitud
from api.pago import Pago, ruta_pago
from api.reporte import Reporte, ruta_Reporte

app.register_blueprint(ruta_Vehiculo,url_prefix = '/api')
app.register_blueprint(ruta_pasajeros, url_prefix = '/api')
app.register_blueprint(ruta_Viaje, url_prefix = '/api')
app.register_blueprint(ruta_solicitud, url_prefix = '/api')
app.register_blueprint(ruta_pago, url_prefix = '/api')
app.register_blueprint(ruta_Reporte, url_prefix = '/api')


@ruta_pago.route('/Relacionpago', methods=['POST'])
def dostabla():
    datos = {}
    resultado = db.session.query(Pasajero,Pago). \
        select_from(Pasajero).join(Pago).all()
    i=0
    for pasajero, pago in resultado:
        i+=1
        datos[i]={
            'pasajero':pasajero.id,
            'pago': pago.idpasajero, 
        }
    return datos

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

@ruta_Viaje.route('/RelacionViaje', methods=['POST'])
def dostabla():
    datos = {}
    resultado = db.session.query(Pasajero,Vehiculo,Viaje). \
        select_from(Pasajero).join(Viaje).all()
    i=0
    for pasajero, vehiculo, viaje  in resultado:
        i+=1
        datos[i]={
            'pasajero':pasajero.id,
            'vehiculo': vehiculo.id, 
        }
    return datos

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

@ruta_solicitud.route('/Relacionsolicitud', methods=['POST'])
def dostabla():
    datos = {}
    resultado = db.session.query(Pasajero,Solicitud). \
        select_from(Pasajero).join(Solicitud).all()
    i=0
    for pasajero, solicitud in resultado:
        i+=1
        datos[i]={
            'pasajero':pasajero.id,
            'solicitud': solicitud.idpasajero, 
        }
    return datos

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')