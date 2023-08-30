import logging

from config import settings


def setup_logging():
    log_level = getattr(logging, settings.LOG_LEVEL.upper())
    logging.basicConfig(level=log_level)


setup_logging()
logger = logging.getLogger(settings.NAME)
