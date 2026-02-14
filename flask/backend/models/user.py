
def validate_login_data(data):
    required_fields = ["matricula", "password"]
    for field in required_fields:
        if field not in data:
            return False, f"El campo '{field}' es obligatorio"
    return True, None