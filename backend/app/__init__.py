from flask import Flask,current_app
from config import Config
from flask_cors import CORS,cross_origin
from app.model import load_model

cors = CORS()

def create_app(config_class = Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    model = load_model()

    cors.init_app(app)

    from app.api.predict import bp as predict_bp
    app.register_blueprint(predict_bp,url_prefix='/predict')

    return app
