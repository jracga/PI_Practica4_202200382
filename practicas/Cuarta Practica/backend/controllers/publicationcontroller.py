from flask import Blueprint, jsonify, request
from db import db
from models.publication import Publication, Comment
from models.user import User
from datetime import datetime

BlueprintPublication = Blueprint('publication', __name__)

# Crear una nueva publicación
@BlueprintPublication.route('/publicaciones/crear', methods=['POST'])
def crearPublicacion():
    user_id = request.json['user_id']
    course_or_professor = request.json['course_or_professor']
    message = request.json['message']
    
    nueva_publicacion = Publication(
        user_id=user_id,
        course_or_professor=course_or_professor,
        message=message,
        creation_date=datetime.utcnow()
    )
    
    db.session.add(nueva_publicacion)
    db.session.commit()
    
    return jsonify({
        'message': 'Publicación creada correctamente',
        'status': 200
    }), 200

# Obtener todas las publicaciones
@BlueprintPublication.route('/publicaciones/obtener', methods=['GET'])
def obtenerPublicaciones():
    publicaciones = Publication.query.all()
    lista_publicaciones = []
    
    for pub in publicaciones:
        lista_publicaciones.append({
            'id': pub.id,
            'user_id': pub.user_id,
            'course_or_professor': pub.course_or_professor,
            'message': pub.message,
            'creation_date': pub.creation_date
        })
        
    return jsonify({
        'publicaciones': lista_publicaciones,
        'status': 200
    }), 200

# Crear un comentario para una publicación
@BlueprintPublication.route('/publicaciones/<int:pub_id>/comentar', methods=['POST'])
def crearComentario(pub_id):
    user_id = request.json['user_id']
    message = request.json['message']
    
    nueva_comentario = Comment(
        publication_id=pub_id,
        user_id=user_id,
        message=message,
        creation_date=datetime.utcnow()
    )
    
    db.session.add(nueva_comentario)
    db.session.commit()
    
    return jsonify({
        'message': 'Comentario agregado correctamente',
        'status': 200
    }), 200
