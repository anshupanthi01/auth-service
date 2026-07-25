class AppError(Exception):
    """Base class for all application-related exceptions."""

    status_code: int = 500
    description: str = "Application error."

    def __init__(self, description: str | None = None):
        self.description = description or self.description
        super().__init__(self.description)


# ==========================================================
# User Errors
# ==========================================================

class UserNotFoundError(AppError):
    status_code = 404
    description = "User not found."


class UsernameAlreadyExistsError(AppError):
    status_code = 409
    description = "Username already exists."


class EmailAlreadyExistsError(AppError):
    status_code = 409
    description = "Email already exists."


class UserVerificationPendingError(AppError):
    status_code = 409
    description = "User verification is pending."


class UserAccountSuspendedError(AppError):
    status_code = 403
    description = "User account is suspended."


class AccountDeletionPendingError(AppError):
    status_code = 409
    description = "Account deletion is pending."


class AccountDeletedError(AppError):
    status_code = 410
    description = "Account has been deleted."


# ==========================================================
# Authentication Errors
# ==========================================================

class InvalidCredentialsError(AppError):
    status_code = 401
    description = "Invalid username/email or password."


class InvalidRefreshTokenError(AppError):
    status_code = 401
    description = "Invalid refresh token."


class InvalidTokenError(AppError):
    status_code = 401
    description = "Invalid authentication token."


class ExpiredTokenError(AppError):
    status_code = 401
    description = "Authentication token has expired."


class MissingTokenError(AppError):
    status_code = 401
    description = "Authentication token is missing."


class UnauthorizedError(AppError):
    status_code = 401
    description = "Authentication required."


class ForbiddenError(AppError):
    status_code = 403
    description = "You do not have permission to perform this action."


# ==========================================================
# Email Verification Errors
# ==========================================================

class EmailNotVerifiedError(AppError):
    status_code = 403
    description = "Email address is not verified."


class VerificationTokenExpiredError(AppError):
    status_code = 400
    description = "Verification token has expired."


class VerificationTokenInvalidError(AppError):
    status_code = 400
    description = "Verification token is invalid."


# ==========================================================
# Password Reset Errors
# ==========================================================

class PasswordResetTokenExpiredError(AppError):
    status_code = 400
    description = "Password reset token has expired."


class PasswordResetTokenInvalidError(AppError):
    status_code = 400
    description = "Password reset token is invalid."


# ==========================================================
# Validation Errors
# ==========================================================

class ValidationError(AppError):
    status_code = 400
    description = "Validation failed."


class BadRequestError(AppError):
    status_code = 400
    description = "Bad request."


# ==========================================================
# Resource Errors
# ==========================================================

class ResourceNotFoundError(AppError):
    status_code = 404
    description = "Requested resource not found."


class ConflictError(AppError):
    status_code = 409
    description = "Resource conflict."


# ==========================================================
# Server Errors
# ==========================================================

class InternalServerError(AppError):
    status_code = 500
    description = "Internal server error."