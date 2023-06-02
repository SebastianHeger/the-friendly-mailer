from enum import Enum


class EnvironmentVariable(str, Enum):
    LOG_LEVEL = "LOG_LEVEL"
    EMAIL_USERNAME_STRATO = "EMAIL_USERNAME_STRATO"
    EMAIL_PASSWORD_STRATO = "EMAIL_PASSWORD_STRATO"
    EMAIL_SENDER_ADDRESS = "EMAIL_SENDER_ADDRESS"
    TRIGGER_HOUR = "TRIGGER_HOUR"
