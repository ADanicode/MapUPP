from flask import Blueprint, request, jsonify
from database.mongo import get_db
from bson import ObjectId

users_bp = Blueprint("users", __name__)

@users_bp.route("/api/login", methods=["POST"])
def login():
    try:
        data = request.json
        if not data or "matricula" not in data or "password" not in data:
            return jsonify({"error": "Faltan matrícula o contraseña"}), 400
        
        db = get_db()
        
        alumno = db.users.find_one({"matricula": data["matricula"]})
        
        if alumno and alumno["password"] == data["password"]:
            
            return jsonify({
                "message": "Bienvenido al Campus UPP",
                "usuario": {
                    "nombre": alumno["name"],
                    "matricula": alumno["matricula"],
                    "grupo": alumno["grupo"]
                }
            }), 200
        
        return jsonify({"error": "Credenciales inválidas"}), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@users_bp.route("/api/users", methods=["POST"])
def create_student():
    """Ruta para registrar nuevos alumnos (útil para tus pruebas)"""
    try:
        data = request.json
        db = get_db()
        
        new_student = {
            "name": data["name"],
            "matricula": data["matricula"],
            "password": data["password"],
            "grupo": data["grupo"] 
        }
        
        result = db.users.insert_one(new_student)
        return jsonify({"message": "Estudiante registrado", "id": str(result.inserted_id)}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500