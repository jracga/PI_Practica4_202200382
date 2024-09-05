# app.py
from flask import Flask, jsonify, request
from flask_cors import CORS
#import mysql.connector

app = Flask(__name__)
CORS(app)  # Permitir todas las solicitudes de cualquier origen

# Configura tu conexión a la base de datos
def get_db_connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='practicas'
    )
    return conn

# Ruta para obtener todos los items
@app.route('/items', methods=['GET'])
def get_items():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM items')
    items = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(items)

# Ruta para crear un nuevo item
@app.route('/items', methods=['POST'])
def create_item():
    new_item = request.json
    name = new_item['name']
    description = new_item['description']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO items (name, description) VALUES (%s, %s)', (name, description))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({
        "status": "success",
        "message": "Item created successfully",
        "data": {
            "name": name,
            "description": description
        }
    }), 201

# Ruta para actualizar un item
@app.route('/items/<int:id>', methods=['PUT'])
def update_item(id):
    updated_item = request.json
    name = updated_item['name']
    description = updated_item['description']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE items SET name = %s, description = %s WHERE id = %s', (name, description, id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({
        "status": "success",
        "message": "Item updated successfully",
        "data": {
            "id": id,
            "name": name,
            "description": description
        }
    }), 204

# Ruta para eliminar un item
@app.route('/items/<int:id>', methods=['DELETE'])
def delete_item(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM items WHERE id = %s', (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({
        "status": "success",
        "message": "Item deleted successfully"
    }), 204

if __name__ == '__main__':
    app.run(debug=True)