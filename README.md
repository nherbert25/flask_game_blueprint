# flask_game_blueprint
plug and play blueprint for a flask application


from flask_game_blueprint import flask_game_blueprint  # Assuming it's pip installable or cloned into your project

app.register_blueprint(flask_game_blueprint)


[tool.poetry]
name = "flask_game_blueprint"
version = "0.1.0"
packages = [{ include = "flask_game_blueprint" }]

poetry build
pip install dist/flask_game_blueprint-0.1.0-py3-none-any.whl



to run as a separate app:
python app.py
It will serve at http://localhost:5001/game