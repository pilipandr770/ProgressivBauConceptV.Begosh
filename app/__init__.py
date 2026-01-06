from flask import Flask
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register blueprints
    from .routes.main import main_bp
    from .routes.innen import innen_bp
    from .routes.aussen import aussen_bp
    from .routes.elektro import elektro_bp
    from .routes.projekt import projekt_bp
    from .routes.booking import booking_bp
    from .routes.contact import contact_bp
    from .routes.footer import footer_bp
    from .chatbot.router import chat_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(innen_bp)
    app.register_blueprint(aussen_bp)
    app.register_blueprint(elektro_bp)
    app.register_blueprint(projekt_bp)
    app.register_blueprint(booking_bp)
    app.register_blueprint(contact_bp)
    app.register_blueprint(footer_bp)
    app.register_blueprint(chat_bp)

    return app