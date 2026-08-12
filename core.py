import sys
from validators import validate_input

def main_loop():
    while True:
        user_input = input('Enter command: ')
        if validate_input(user_input):
            process_command(user_input)
        else:
            print('Invalid command. Please try again.')


def process_command(command):
    print(f'Processing command: {command}')

if __name__ == '__main__':
    main_loop()