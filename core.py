import time

class Game:
    def __init__(self, name, max_players):
        self.name = name
        self.max_players = max_players
        self.players = []

    def add_player(self, player):
        if len(self.players) < self.max_players:
            self.players.append(player)
            return True
        return False

    def start_game(self):
        if len(self.players) == self.max_players:
            print(f'Starting game: {self.name}')
        else:
            print('Not enough players to start.')

class Performance:
    @staticmethod
    def measure_execution_time(func):
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            print(f'Execution time: {end_time - start_time:.4f} seconds')
            return result
        return wrapper

@Performance.measure_execution_time
def game_logic(game):
    print(f'Playing {game.name}')
    time.sleep(1)  # Simulate game processing

if __name__ == '__main__':
    game = Game('Adventure Quest', 4)
    game.add_player('Player1')
    game.add_player('Player2')
    game.add_player('Player3')
    game.add_player('Player4')
    game.start_game()
    game_logic(game)