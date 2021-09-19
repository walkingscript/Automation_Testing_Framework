def init_logging():
    from logging.config import dictConfig
    from .settings import LOGGER_CONFIGURATION
    dictConfig(LOGGER_CONFIGURATION)
