from flask import Blueprint

flask_game_bp = Blueprint(
    "flask_game_bp",
    __name__,
    template_folder="../templates/game",
    static_folder="../static",
    static_url_path="/flask_game_blueprint/static",
)

from . import routes
