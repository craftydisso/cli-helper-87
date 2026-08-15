import sys

class InputError(Exception):
    pass

def validate_input(user_input):
    if not user_input.isdigit() or int(user_input) < 1:
        raise InputError("Input must be a positive integer.")
    return int(user_input)

def main():
    while True:
        user_input = input("Enter a positive integer (or 'q' to quit): ")
        if user_input.lower() == 'q':
            print("Exiting...")
            break
        try:
            validated_input = validate_input(user_input)
            print(f"You entered: {validated_input}")
        except InputError as e:
            print(e)

if __name__ == '__main__':
    main()