class AppError(Exception):
    """Base class for all Appentication-related exceptions."""
    def __init__(self, status_code: int, description: str):
        self.status_code = status_code
        self.description = description


# ===== User =====

class UserNotFoundError(AppError):
    pass

class UsernameAlreadyExistsError(AppError):
    pass

class EmailAlreadyExistsError(AppError):
    pass

# ===== Authentication =====

class InvalidCredentialsError(AppError):
    pass

class InvalidRefreshTokenError(AppError):
    pass

class InvalidTokenError(AppError):
    pass

class ExpiredTokenError(AppError):
    pass