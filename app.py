from flask import Flask
from flask_game_blueprint import flask_game_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(flask_game_bp)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5001)
