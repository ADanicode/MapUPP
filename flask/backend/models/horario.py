def validate_horario_data(data):
    
    required_fields = ["materia", "aula", "horario", "dia", "grupo", "coordinates"]
    
    for field in required_fields:
        if field not in data:
            return False, f"El campo '{field}' es obligatorio"
    if not isinstance(data["coordinates"], list) or len(data["coordinates"]) != 2:
        return False, "El campo 'coordinates' debe ser una lista con [Long, Lat]"
        
    return True, None