from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint raíz que devuelve un mensaje de bienvenida
@app.route('/', methods=['GET'])
def welcome():
    return "Bienvenido al servidor de prueba!"

# Endpoint que acepta datos en formato JSON y devuelve una confirmación
@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json  # Obtiene los datos JSON enviados en la petición
    # Aquí puedes procesar los datos según sea necesario
    return jsonify({'message': 'Datos recibidos con éxito!', 'yourData': data})

# Endpoint que devuelve el estado del servidor
@app.route('/status', methods=['GET'])
def server_status():
    return jsonify({'status': 'Activo'})

if __name__ == '__main__':
    app.run(debug=True)  # Inicia el servidor en modo de depuración
