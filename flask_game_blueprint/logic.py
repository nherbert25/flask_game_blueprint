class GameSession:
    def __init__(self, player_name):
        self.player_name = player_name
        self.hp = 100
        self.attack = 2
        self.defense = 5
        self.enemies = []

    def attack(self, enemy):
        # Dummy logic
        return f"{self.player_name} attacks {enemy}!"
