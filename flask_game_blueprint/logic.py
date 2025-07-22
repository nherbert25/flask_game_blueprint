class Player:
    def __init__(self, player_name):
        self.player_name = player_name
        self.hp = 100
        self.attack_stat = 2
        self.defense = 5
        self.enemies = []

    def attack(self, enemy):
        # Dummy logic
        return f"{self.player_name} attacks {enemy}!"


class Enemy:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.image_url = f"/flask_game_blueprint/static/images/{name}.jpg"

    def __repr__(self):
        return f"Enemy(name={self.name}, hp={self.hp}, attack={self.attack}, defense={self.defense})"
