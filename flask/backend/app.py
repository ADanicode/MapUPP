from flask import Flask
from flask_cors import CORS
from config import Config
from routes.users import users_bp
from routes.horarios import horarios_bp 

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)
    
    app.register_blueprint(users_bp)
    app.register_blueprint(horarios_bp)
    
    return app

app = create_app()

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)