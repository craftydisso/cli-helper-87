import json
import os

class ConfigLoader:
    def __init__(self, default_config):
        self.default_config = default_config
        self.config = default_config.copy()

    def load(self, filepath):
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                user_config = json.load(file)
                self.config.update(user_config)

    def get(self, key, default=None):
        return self.config.get(key, default)

if __name__ == '__main__':
    defaults = {
        'resolution': '1920x1080',
        'fullscreen': True,
        'volume': 100
    }
    loader = ConfigLoader(defaults)
    loader.load('config.json')
    print(loader.get('resolution'))
    print(loader.get('fullscreen'))
    print(loader.get('music_volume', 50))