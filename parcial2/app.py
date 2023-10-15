from flask import Flask, jsonify,json
from config.db import  db, ma, app
from api.vehiculo import Vehiculo, ruta_Vehiculo
from api.pasajero import Pasajero, ruta_pasajeros
from api.viajes import Viaje, ruta_Viaje
from api.solicitud import Solicitud, ruta_solicitud
from api.pago import Pago, ruta_pago
from api.reporte import Reporte, ruta_Reporte

app.register_blueprint(ruta_Vehiculo,url_prefix = '/api')
app.register_blueprint(ruta_pasajeros, url_prefix = '/api' )
app.register_blueprint(ruta_Viaje, url_prefix = '/api')
app.register_blueprint(ruta_solicitud, url_prefix = '/api')
app.register_blueprint(ruta_pago, url_prefix = '/api')
app.register_blueprint(ruta_Reporte, url_prefix = '/api')



@app.route('/')
def index():
    return "Hola Mundo"

@app.route('/dostablas', methods=['POST'])
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



if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')