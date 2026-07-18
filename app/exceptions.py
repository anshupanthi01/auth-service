class AppError(Exception):
    """Base class for all Appentication-related exceptions."""


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