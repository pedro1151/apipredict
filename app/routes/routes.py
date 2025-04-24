from flask import Blueprint, request, jsonify
from models.models import Usuario, Roles
from schema.schemas import rolesSchema
import bcrypt
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from database import db
blue_print = Blueprint('app',  __name__)


#Ruta de inicio
@blue_print.route('/', methods = ['GET'])
def inicio():
    return jsonify(respuesta = 'Rest API Predict by Pedro Ramos, VERSION 1.0')


#Ruta de registro de usurio
@blue_print.route('/auth/register', methods = ['POST'])
def register():
    try:
        #Obtener usuario
        email    = request.json.get('email')
        password = request.json.get('password')
  
        if not email or not password:
            return jsonify(respuesta = 'Campos invalidos'), 400

        #Consulto en la Db

        existe_usuario = Usuario.query.filter_by(email = email).first()
        mess_error = 'Paso existe usuario'
        if existe_usuario:
            return jsonify(respuesta = 'El usuario ya existe'), 400

        #Encriptamo wl password del usuario y lo creamos
        pass_encriptada = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        mess_error = 'Paso pas encriptada'
        #Creamos para guardar en DB

        nuevo_usuario = Usuario(email, pass_encriptada)
        mess_error = 'Paso nuevo usuario(0)'
        db.session.add(nuevo_usuario)
        mess_error = 'Paso nuevo usuario (1)'
        db.session.commit()
        mess_error = 'Paso nuevo usuario (2)'

        return jsonify(respuesta = 'Usuario creado exitosamente'), 200
    except Exception:
        return jsonify(respuesta = 'Error General en la peticion'+mess_error),500

#Ruta para Login
@blue_print.route('/auth/login', methods = ['POST'])
def login():
    try:
        #Obtener usuario
        email    = request.json.get('email')
        password = request.json.get('password')

        if not email or not password:
            return jsonify(respuesta = 'Campos invalidos'), 400

        #Consulto en la Db

        existe_usuario = Usuario.query.filter_by(email = email).first()

        if not existe_usuario:
            return jsonify(respuesta = 'El usuario NO existe'), 400

        es_clave_valida = bcrypt.checkpw(password.encode('utf-8'), existe_usuario.password.encode('utf-8'))

        if es_clave_valida:
            access_token = create_access_token(identity=email)
            return jsonify(access_token = access_token, email = email ), 200
            
        
        return jsonify(respuesta = 'Clave o usuario incorrecto/s'),404
   
    except Exception:
        return jsonify(respuesta = 'Error General en la peticion'),500

# rutas protegidas por jwt
#get roles
@blue_print.route('/api/roles', methods = ['GET'])
@jwt_required()
def getRoles():
    try:
        roles    = Roles.query.all()
        response = rolesSchema.dump(roles)
        return rolesSchema.jsonify(response),  200
    except Exception:
        return jsonify(response= 'Error al recuperar los roles'), 500


        
#Ruta Crear Rol
@blue_print.route('/api/roles', methods = ['POST'])
@jwt_required()
def createRol():
    try:
        #Obtener usuario
        codigo  = request.json.get('codigo')
        name    = request.json.get('name')
        image   = request.json.get('image')
        route   = request.json.get('route')
  
        if not codigo or not name or not image or not route:
            return jsonify(respuesta = 'Campos invalidos o nulos'), 400

        #Consulto en la Db

        existe_rol = Roles.query.filter_by(codigo = codigo).first()
   
        if existe_rol:
            return jsonify(respuesta = 'El rol ya existe'), 400

        

        nuevo_rol = Roles(codigo, name, image, route)
        db.session.add(nuevo_rol)
        db.session.commit()

        return jsonify(respuesta = 'Rol creado exitosamente'), 200
    except Exception:
        return jsonify(respuesta = 'Error General en la peticion'),500


   