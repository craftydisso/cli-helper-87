import re

class InputValidationError(Exception):
    pass

def validate_input(user_input):
    if not isinstance(user_input, str):
        raise InputValidationError("Input must be a string.")
    if len(user_input) == 0:
        raise InputValidationError("Input cannot be empty.")
    if not re.match("^[a-zA-Z0-9_]*$, user_input):
        raise InputValidationError("Input can only contain alphanumeric characters and underscores.")
    return True
