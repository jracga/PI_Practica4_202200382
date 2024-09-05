from controllers.estructuras import users
from flask import Blueprint, jsonify, request
from models.user import User

BlueprintUser = Blueprint('user', __name__)
user_logueado = ''

#METODOS DE REGISTRO -------------------------------------------
#Metodo para registrar un usuario a la lista de usuarios

@BlueprintUser.route('/usuarios/registrar', methods=['POST'])
def registrarUsuario():
    global users
    id = request.json['id']
    registroA = request.json['registroA']
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    password = request.json['password']
    email = request.json['email']
    nuevo = User(id, registroA, nombre, apellido, password, email)
    users.append(nuevo)
    return jsonify({
        'message':'Usuario registrado correctamente',
        'status':200
    }), 200
    
#Metodo para obtener todos los usuarios
@BlueprintUser.route('/usuarios/obtener', methods=['GET'])
def obtenerUsuarios():
    global users
    lista = []
    for user in users:
        lista.append({
            'id':user.id,
            'registroA':user.registroA,
            'nombre':user.nombre,
            'apellido':user.apellido,
            'password':user.password,
            'email':user.email
        })
    return jsonify({
        'usuarios':lista,
        'status':200
    }), 200

#Metodo para actualizar la contraseña de un usuario por medio de su registroA o email
@BlueprintUser.route('/usuarios/actualizarPassword', methods=['PUT'])
def actualizarPassword():
    global users
    registroA = request.json['registroA']
    email = request.json['email']
    password = request.json['password']
    for user in users:
        if user.registroA == registroA or user.email == email:
            user.password = password
            return jsonify({
                'message':'Contraseña actualizada correctamente',
                'status':200
            }), 200
    return jsonify({
        'message':'Usuario no encontrado',
        'status':404
    }), 404


#Metodo para loguear un usuario que ya se encuentra registrado por medio de su registroA o email 
@BlueprintUser.route('/usuarios/login', methods=['POST'])
def login():
    global users
    global user_logueado
    registroA = request.json['registroA']
    email = request.json['email']
    password = request.json['password']
    for user in users:
        if user.registroA == registroA or user.email == email:
            if user.password == password:
                user_logueado = user
                return jsonify({
                    'message':'Usuario logueado correctamente',
                    'status':200
                }), 200
            return jsonify({
                'message':'Contraseña incorrecta',
                'status':400
            }), 400
    return jsonify({
        'message':'Usuario no encontrado',
        'status':404
    }), 404
