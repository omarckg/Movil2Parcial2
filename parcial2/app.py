from flask import Flask, jsonify,json
from config.db import  db, ma, app
from api.vehiculo import Vehiculo, VehiculosSchema
from api.pasajero import Pasajero, PasajerosSchema
from api.reporte import Reporte, ReportesSchema

#app.register_blueprint(ruta_Vehiculo,url_prefix = '/api')
#app.register_blueprint(ruta_pasajeros, url_prefix = '/api')


@app.route('/')
def index():
    return "Hola Mundo"

@app.route('/dostablas', methods=['POST'])
def dostabla():
    datos = {}
    resultado = db.session.query(Cliente,Reserva). \
        select_from(Cliente).join(Reserva).all()
    i=0
    for clientes, reservas in resultado:
        i+=1
        datos[i]={
            'cliente':clientes.nombre,
            'reserva': reservas.id, 
        }
    return datos

@app.route('/dostablas1', methods=['POST'])
def dostabla1():
    datos = {}
    resultado = db.session.query(Aerolinea,Avion). \
        select_from(Aerolinea).join(Avion).all()
    i=0
    for aerolinea,avion in resultado:
        i+=1
        datos[i]={
            'aerolinea':aerolinea.nombre,
            'avion':avion.id,
        }
    return datos

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')