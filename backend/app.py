from flask import Flask, request, jsonify
from flask_cors import CORS
from bd import db, Usuario,TiposEdificios,MisEdificios
from datetime import timedelta


app = Flask(__name__)
CORS(app)


# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Franco@localhost/tpintro'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Inicialización de la extensión SQLAlchemy
db.init_app(app)
with app.app_context():
    db.create_all()


# Ruta para manejar la autenticación/login
@app.route('/login', methods=['GET'])
def login():
#Hago un select de todos los usuarios para trabajarlo en el js
    usuarios = Usuario.query.all()
    usuarios_list = [{'nombre': usuario.nombre, 'contraseña': usuario.contraseña, 'id': usuario.id} for usuario in usuarios]
    return usuarios_list



# Ruta para manejar la autenticación/signIn
@app.route('/signIn', methods=['POST'])
def signIn():
    #agarra los parametros de la url
    usuario = request.args.get('usuario')
    contraseña = request.args.get('contraseña')
    #hace un select * para poder saber el ultimo id de los usuarios
    usuarios = Usuario.query.all()
    usuarios_list = [{'id': usuario.id, 'nombre': usuario.nombre, 'contraseña': usuario.contraseña, 'plata':0} for usuario in usuarios]
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


# Ruta para que me devuelva un usuario segun el id
@app.route('/selectById', methods=['get'])
def selectById():
    
    id = request.args.get('id')
    
    usuario = Usuario.query.get(id)
    print(usuario.nombreciudad)
    return jsonify({
                'id': usuario.id,
                'nombre': usuario.nombre,
                'contraseña': usuario.contraseña,
                'imagen': usuario.imagen,
                'plata': usuario.plata,
                'nombreciudad': usuario.nombreciudad
            })

            
@app.route('/updateProfile', methods=['PUT'])
def updateProfile():
    
    data = request.get_json()
    id = data.get('id')
    nombre = data.get('nombre')
    imagen = data.get('imagen')
    nombreCiudad = data.get('nombreCiudad')
    # Verificar si existe otro usuario con el mismo nombre
    existing_user = Usuario.query.filter(Usuario.nombre == nombre).filter(Usuario.id != id).first()
    if existing_user:
        return jsonify({'message': 'Ya existe un usuario con ese nombre','error':400}), 400
    
    # Obtener el usuario desde la base de datos
    usuario = Usuario.query.get(id)
    if usuario:
        usuario.nombre = nombre
        usuario.imagen = imagen
        usuario.nombreciudad=nombreCiudad
        db.session.commit()
        return jsonify({'message': 'Perfil actualizado exitosamente'}), 200
    else:
        return jsonify({'message': 'Usuario no encontrado'}), 404


@app.route('/selectTiposEdificios', methods=['GET'])
def selectTiposEdificios():
    tipoEdificios = TiposEdificios.query.all()
    listaTipoEdificios = [{
        'id': tipo.id,
        'nombre': tipo.nombre,
        'imagen': tipo.imagen,
        'clase': tipo.clase,
        'poblacion': tipo.poblacion,
        'precio': tipo.precio,
        'descripcion': tipo.descripcion,
        'tiemporecaudacion': str(tipo.tiemporecaudacion),  # Convertir timedelta a str
        'platarecaudacion': tipo.platarecaudacion
    } for tipo in tipoEdificios]
  
    return jsonify(listaTipoEdificios)

@app.route('/comprarEdificio', methods=['post'])
def comprarEdificio():
    
    idEdificio = request.args.get('idEdificio')
    idUsuario = request.args.get('idUsuario')
    #Resto la plata de lo que sale el edificio al usuario
    usuario = Usuario.query.get(idUsuario)
    edificio = TiposEdificios.query.get(idEdificio)
    usuario.plata=usuario.plata-edificio.precio
    #creo en la tabla misedificios una fila con el nuevo edificio del usuario
    misEdificios = MisEdificios.query.all()
    max_id = 0
    for aux in misEdificios:
        if aux.id > max_id:
            max_id = aux.id
    max_id=max_id+1 
  
    miEdificio = MisEdificios(id=max_id, nombre=edificio.nombre, imagen=edificio.imagen,clase=edificio.clase,poblacion=edificio.poblacion,descripcion=edificio.descripcion,tiemporecaudacion=edificio.tiemporecaudacion,platarecaudacion=edificio.platarecaudacion,valor=edificio.precio,idusuario=idUsuario,idtipoedificio=idEdificio)
    db.session.add(miEdificio)
    db.session.commit()

    return {'message': 'Edificio comprado','comprado': 'si'}


# Función para formatear timedelta
def format_timedelta(td):
    total_seconds = int(td.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"

@app.route('/selectMisEdificios', methods=['GET'])
def selectMisEdificios():
    idusuario = request.args.get('id')
    misEdificios = MisEdificios.query.filter_by(idusuario=idusuario).all()
    print(misEdificios)
    listaTipoEdificios = [{
        'id': miEdificio.id,
        'nombre': miEdificio.nombre,
        'imagen': miEdificio.imagen,
        'clase': miEdificio.clase,
        'poblacion': miEdificio.poblacion,
        'descripcion': miEdificio.descripcion,
        'tiemporecaudacion': format_timedelta(miEdificio.tiemporecaudacion),
        'valor': miEdificio.valor,
        'platarecaudacion': miEdificio.platarecaudacion,
        'idtipoedificio': miEdificio.idtipoedificio,
    } for miEdificio in misEdificios]
  
    return jsonify(listaTipoEdificios)

@app.route('/recaudar', methods=['PUT'])
def recaudar():
    idUsuario = request.args.get('idUsuario')
    idEdificio = request.args.get('idEdificio')
    usuario = Usuario.query.get(idUsuario)
    edificio = MisEdificios.query.get(idEdificio)
    usuario.plata = usuario.plata+edificio.platarecaudacion
    db.session.commit()
    return jsonify({'message': 'Plata recaudada correctamente','idEdificio':idEdificio,'plata':usuario.plata}), 200


@app.route('/deleteMisEdificiosById', methods=['DELETE'])
def deleteMisEdificiosById():
    idEdificio = request.args.get('idEdificio')
    edificio = MisEdificios.query.get(idEdificio)
    db.session.delete(edificio)
    db.session.commit()
    return jsonify({'message': 'El edificio fue eliminado'}), 200

@app.route('/updateMiEdificio', methods=['PUT'])
def updateMiEdificio():
    
    data = request.get_json()
    id = data.get('id')
    nombre = data.get('nombre')
    imagen = data.get('imagen')
    descripcion = data.get('descripcion')
    
    miEdificio = MisEdificios.query.get(id)
    if miEdificio:
        miEdificio.nombre = nombre
        miEdificio.imagen = imagen
        miEdificio.descripcion = descripcion
        db.session.commit()
        return jsonify({'message': 'Edificio actualizado correctamente'}), 200
    else:
        return jsonify({'message': 'Edificio no encontrado'}), 404

@app.route('/mejorarEdificio', methods=['PUT'])
def mejorarEdificio():
    
    data = request.get_json()
    idUsuario = data.get('idUsuario')
    idEdificio = data.get('idEdificio')
    usuario = Usuario.query.get(idUsuario)
    miEdificio = MisEdificios.query.get(idEdificio)
    usuario.plata=usuario.plata-miEdificio.valor
    miEdificio.valor=miEdificio.valor*2
    if(miEdificio.clase=='C'):
        miEdificio.poblacion=miEdificio.poblacion*2
    
    elif(miEdificio.clase=='S'):
        miEdificio.platarecaudacion=miEdificio.platarecaudacion*2

    db.session.commit()

    return jsonify({'message': 'Edificio actualizado correctamente'}), 200




if __name__ == '__main__':
    app.run(debug=True)
