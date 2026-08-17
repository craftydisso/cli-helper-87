import json

class GameError(Exception):
    pass

class FileNotFoundError(GameError):
    pass

class InvalidInputError(GameError):
    pass

def load_game_data(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"File {file_path} not found.")
    except json.JSONDecodeError:
        raise GameError(f"Failed to decode JSON from {file_path}.")


def validate_input(user_input, valid_options):
    if user_input not in valid_options:
        raise InvalidInputError("Input is not valid.")


def main():
    try:
        data = load_game_data('game_data.json')
        validate_input('example', data['options'])
    except GameError as e:
        print(e)

if __name__ == '__main__':
    main()