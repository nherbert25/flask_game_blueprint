from flask import Blueprint

flask_game_bp = Blueprint(
    "flask_game_bp",
    __name__,
    template_folder="../templates/game",
    static_folder="../static/game",
    static_url_path="/game/static"
)

from . import routes
