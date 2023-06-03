import logging
import os

from enums import EnvironmentVariable

logger = logging
logger.basicConfig(
    format="%(asctime)s [%(levelname)s]: %(message)s",
    level=os.getenv(EnvironmentVariable.LOG_LEVEL, "DEBUG").upper(),
    handlers=[logger.StreamHandler()],
)
