from flask import render_template, request, jsonify
from . import flask_game_bp
from .logic import Player, Enemy

# Dummy in-memory state
sessions = {}


@flask_game_bp.route("/", methods=["GET"])
@flask_game_bp.route("/game", methods=["GET"])
def game_home():
    return render_template("index.html")


@flask_game_bp.route("/game/start", methods=["POST"])
def start_game():
    player_name = request.json.get("player_name", "Player1")
    player = Player(player_name)
    enemy = Enemy(name="slime", hp=30, attack=5, defense=0)
    sessions[player_name] = player
    return jsonify(
        {
            "enemy": {
                "name": enemy.name,
                "image_url": enemy.image_url,
                "hp": enemy.hp,
                "attack": enemy.attack,
                "defense": enemy.defense,
            },
            "player": {
                "name": player.player_name,
                "hp": player.hp,
                "attack": player.attack_stat,
                "defense": player.defense,
            },
            "message": f"Game started for {player_name}!",
        }
    )


@flask_game_bp.route("/game/attack", methods=["POST"])
def attack():
    player_name = request.json["player_name"]
    enemy = request.json["enemy"]
    session = sessions.get(player_name)
    if not session:
        return jsonify({"error": "No active session"}), 400
    result = session.attack(enemy)
    return jsonify({"result": result})
