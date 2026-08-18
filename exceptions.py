class GameError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidInputError(GameError):
    pass

class ResourceNotFoundError(GameError):
    pass

class OperationFailedError(GameError):
    def __init__(self, message, errors=None):
        super().__init__(message)
        self.errors = errors

class ConfigurationError(GameError):
    def __init__(self, message, config_key):
        super().__init__(message)
        self.config_key = config_key


def handle_error(error):
    if isinstance(error, InvalidInputError):
        return {'error': 'Invalid input', 'message': str(error)}
    elif isinstance(error, ResourceNotFoundError):
        return {'error': 'Resource not found', 'message': str(error)}
    elif isinstance(error, OperationFailedError):
        return {'error': 'Operation failed', 'message': str(error), 'details': error.errors}
    elif isinstance(error, ConfigurationError):
        return {'error': 'Configuration error', 'message': str(error), 'key': error.config_key}
    return {'error': 'Unknown error', 'message': str(error)}