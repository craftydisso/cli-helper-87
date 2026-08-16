class GameProcessor:
    def __init__(self, game_data):
        self.game_data = game_data

    def start_processing(self):
        self.validate_data()
        self.perform_calculations()

    def validate_data(self):
        if not self.game_data:
            raise ValueError('Game data cannot be empty')

    def perform_calculations(self):
        # Placeholder for actual calculations
        print('Processing game data...')

if __name__ == '__main__':
    game_data_sample = {'score': 100, 'level': 5}
    processor = GameProcessor(game_data_sample)
    processor.start_processing()