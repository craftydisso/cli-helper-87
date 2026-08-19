import random

class Game:
    def __init__(self, name, max_players):
        self.name = name
        self.max_players = max_players
        self.current_players = []

    def add_player(self, player):
        if len(self.current_players) < self.max_players:
            self.current_players.append(player)
            return True
        return False

    def remove_player(self, player):
        if player in self.current_players:
            self.current_players.remove(player)
            return True
        return False

    def start_game(self):
        if len(self.current_players) > 1:
            print(f"Starting game: {self.name}")
        else:
            print("Not enough players to start the game.")

    def get_random_player(self):
        if self.current_players:
            return random.choice(self.current_players)
        return None
