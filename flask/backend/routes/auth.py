from flask import Blueprint, request, jsonify
from database.mongo import get_db

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/api/login", methods=["POST"])
def login():
    try:
        data = request.json
       
        if not data or "matricula" not in data or "password" not in data:
            return jsonify({"error": "Faltan credenciales"}), 400
        
        db = get_db()
        alumno = db.users.find_one({"matricula": data["matricula"]})
        
        if alumno and alumno["password"] == data["password"]:
            return jsonify({
                "message": "Login exitoso",
                "usuario": {
                    "nombre": alumno["name"],
                    "matricula": alumno["matricula"],
                    "grupo": alumno["grupo"] 
                }
            }), 200
        else:
            return jsonify({"error": "Matrícula o contraseña incorrectos"}), 401
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500