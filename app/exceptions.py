class AppError(Exception):
    """Base class for all Appentication-related exceptions."""
    def __init__(self, status_code: int, description: str):
        self.status_code = status_code
        self.description = description


# ===== User =====

class UserNotFoundError(AppError):
    pass

class UsernameAlreadyExistsError(AppError):
    def __init__(self, description: str = "Username already exists."):
        super().__init__(409, description)

class EmailAlreadyExistsError(AppError):
    def __init__(self, description: str = "Email already exists."):
        super().__init__(409, description)

class UserVerificationPending(AppError):
    def __init__(self, description: str = "User verification is pending."):
            super().__init__(409, description)
class UserAccountSuspended(AppError):
    def __init__(self, description: str = "User account is suspended."):
            super().__init__(409, description)

class AccountDeletionPending(AppError):
    def __init__(self, description: str = "Account deletion is pending."):
            super().__init__(409, description)

class AccountDeleted(AppError):
    def __init__(self, description: str = "Account deleted."):
            super().__init__(409, description)

# ===== Authentication =====

class InvalidCredentialsError(AppError):
    pass

class InvalidRefreshTokenError(AppError):
    pass

class InvalidTokenError(AppError):
    pass

class ExpiredTokenError(AppError):
    pass