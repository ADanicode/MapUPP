from flask import Blueprint, request, jsonify
from database.mongo import get_db
from models.horario import validate_horario_data

horarios_bp = Blueprint("horarios", __name__)

@horarios_bp.route("/api/horarios/<grupo>", methods=["GET"])
def get_horarios_by_grupo(grupo):
    
    try:
        db = get_db()
        
        clases = list(db.horarios.find({"grupo": grupo}))
        
        for clase in clases:
            clase["_id"] = str(clase["_id"])
            
        return jsonify(clases), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@horarios_bp.route("/api/horarios", methods=["POST"])
def create_horario():
    """
    Ruta para insertar las clases en la base de datos (puedes usarla con Postman) [cite: 812]
    """
    try:
        data = request.json
        
        is_valid, error = validate_horario_data(data)
        
        if not is_valid:
            return jsonify({"error": error}), 400
            
        db = get_db()
        result = db.horarios.insert_one(data)
        return jsonify({"message": "Clase registrada", "id": str(result.inserted_id)}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500