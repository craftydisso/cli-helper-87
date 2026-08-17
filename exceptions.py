class GameDataError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class InvalidScoreError(GameDataError):
    def __init__(self, score):
        super().__init__(f'Invalid score: {score}')

class PlayerNotFoundError(GameDataError):
    def __init__(self, player_name):
        super().__init__(f'Player not found: {player_name}')

class GameNotInitializedError(GameDataError):
    def __init__(self):
        super().__init__('Game has not been initialized')

class DataFormatError(GameDataError):
    def __init__(self, value):
        super().__init__(f'Incorrect data format: {value}')