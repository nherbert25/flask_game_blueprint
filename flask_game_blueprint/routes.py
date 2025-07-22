from flask import render_template, request, jsonify
from . import game_bp
from .logic import GameSession

# Dummy in-memory state
sessions = {}

@game_bp.route("/game", methods=["GET"])
def game_home():
    return render_template("index.html")

@game_bp.route("/game/start", methods=["POST"])
def start_game():
    player_name = request.json.get("player_name", "Player1")
    session = GameSession(player_name)
    sessions[player_name] = session
    return jsonify({"message": f"Game started for {player_name}!"})

@game_bp.route("/game/attack", methods=["POST"])
def attack():
    player_name = request.json["player_name"]
    enemy = request.json["enemy"]
    session = sessions.get(player_name)
    if not session:
        return jsonify({"error": "No active session"}), 400
    result = session.attack(enemy)
    return jsonify({"result": result})
