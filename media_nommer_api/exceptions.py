class InvalidInputError(Exception):
    """
    Raised when an invalid argument is passed to an API client method.
    """
    message = 'Invalid input.'