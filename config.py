import json
import os

class ConfigLoader:
    def __init__(self, default_config_path):
        self.default_config_path = default_config_path
        self.config = self.load_default_config()

    def load_default_config(self):
        if os.path.exists(self.default_config_path):
            with open(self.default_config_path, 'r') as f:
                return json.load(f)
        return {}

    def get(self, key, default=None):
        return self.config.get(key, default)

if __name__ == '__main__':
    config_loader = ConfigLoader('default_config.json')
    print(config_loader.get('setting1', 'default_value'))
