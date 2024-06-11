from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/login', methods=['GET'])
def login():
    # Obtener los datos del formulario de la URL
    usuario = request.args.get('usuario')
    contraseña = request.args.get('contraseña')

    # Realizar aquí la lógica de autenticación o lo que necesites hacer con los datos
    
    # Por ahora, solo devuelve un mensaje para confirmar que se recibieron los datos
    return f'Usuario: {usuario}, Contraseña: {contraseña}'

if __name__ == '__main__':
    app.run(debug=True)
