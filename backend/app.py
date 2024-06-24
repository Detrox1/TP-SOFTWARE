from flask import Flask, request
from flask_cors import CORS
from bd import db, Usuario

app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Franco@localhost/tpintro'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialización de la extensión SQLAlchemy
db.init_app(app)
with app.app_context():
    db.create_all()

# Habilitar CORS para todos los dominios
CORS(app)

# Ruta para manejar la autenticación/login
@app.route('/login', methods=['GET'])
def login():
    # Obtener los datos del formulario de la URL 
    usuario = request.args.get('usuario')
    contraseña = request.args.get('contraseña')

#Hago un select de todos los usuarios para trabajarlo en el js
    usuarios = Usuario.query.all()
    usuarios_list = [{'nombre': usuario.nombre, 'contraseña': usuario.contraseña} for usuario in usuarios]
    

    return usuarios_list



# Ruta para manejar la autenticación/signIn
@app.route('/signIn', methods=['POST'])
def signIn():
    #agarra los parametros de la url
    usuario = request.args.get('usuario')
    contraseña = request.args.get('contraseña')
    #hace un select * para poder saber el ultimo id de los usuarios
    usuarios = Usuario.query.all()
    usuarios_list = [{'id': usuario.id, 'nombre': usuario.nombre, 'contraseña': usuario.contraseña} for usuario in usuarios]
    id=len(usuarios_list)+1
    #verifica si existe un usario con el mismo nombre
    for aux in usuarios:
        if aux.nombre == usuario:
            return {'message': 'El nombre de usuario ya existe','creado': 'no'}
        



    #crea e inserta el nuevo usarios
    nuevo_usuario = Usuario(id=id, nombre=usuario, contraseña=contraseña)
    db.session.add(nuevo_usuario)
    db.session.commit()

    return {'message': 'Usuario creado exitosamente','creado': 'si', 'usuario': {'id': nuevo_usuario.id, 'nombre': nuevo_usuario.nombre}}



if __name__ == '__main__':
    app.run(debug=True)
