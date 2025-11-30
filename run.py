from flask import Flask
from models.modelo import db
from controllers.views import bp as tasks_bp


def create_app() -> Flask:
    """Instancia e configura a aplicação Flask."""
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.secret_key = "chave-secreta"

    db.init_app(app)
    app.register_blueprint(tasks_bp)

    return app


if __name__ == "__main__":
    application = create_app()

    with application.app_context():
        db.create_all()

    application.run(debug=True)
