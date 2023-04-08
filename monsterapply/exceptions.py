class BaseMonsterException(Exception):
    """Base exception for all Monster exceptions."""

class TimeOutException(BaseMonsterException):
    """If bot has been running too long and the session times out."""
