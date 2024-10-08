from db import db #nuevo 
from flask import Blueprint, jsonify, request
from models.user import User
from werkzeug.security import check_password_hash, generate_password_hash

BlueprintUser = Blueprint('user', __name__)

@BlueprintUser.route('/registrar', methods=['POST'])
def registrarUsuario():
    try:
        data = request.json

        # Verificar si el email ya existe
        existing_user = User.query.filter_by(email=data['email']).first()
        if existing_user:
            return jsonify({
                'message': 'El correo electrónico ya está registrado.',
                'status': 400
            }), 400

        nuevo = User(
            registroA=data['registroA'],
            nombre=data['nombre'],
            apellido=data['apellido'],
            password=data['password'],
            email=data['email']
        )
        db.session.add(nuevo)
        db.session.commit()
        return jsonify({
            'message': 'Usuario registrado correctamente',
            'status': 200
        }), 200
    except Exception as e:
        return jsonify({
            'message': str(e),
            'status': 500
        }), 500

@BlueprintUser.route('/obtener', methods=['GET'])
def obtenerUsuarios():
    users = User.query.all()
    lista = []
    for user in users:
        lista.append({
            'id': user.id,
            'registroA': user.registroA,
            'nombre': user.nombre,
            'apellido': user.apellido,
            'password': user.password,
            'email': user.email
        })
    return jsonify({
        'usuarios': lista,
        'status': 200
    }), 200

@BlueprintUser.route('/actualizarPassword', methods=['PUT'])
def actualizarPassword():
    data = request.json
    user = User.query.filter((User.registroA == data['registroA']) | (User.email == data['email'])).first()
    if user:
        user.password = data['password']
        db.session.commit()
        return jsonify({
            'message': 'Contraseña actualizada correctamente',
            'status': 200
        }), 200
    return jsonify({
        'message': 'Usuario no encontrado',
        'status': 404
    }), 404

@BlueprintUser.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter((User.registroA == data['registroA']) | (User.email == data['email'])).first()
    if user:
        if check_password_hash(user.password, data['password']):
            return jsonify({
                'message': 'Usuario logueado correctamente',
                'status': 200
            }), 200
        return jsonify({
            'message': 'Contraseña incorrecta',
            'status': 400
        }), 400
    return jsonify({
        'message': 'Usuario no encontrado',
        'status': 404
    }), 404