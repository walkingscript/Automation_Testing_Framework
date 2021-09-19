from datetime import datetime
from os.path import normpath, join

from framework import config
from .filters import CredentialsFilter

verbose_log_folder = normpath(config.LOGS_DIRECTORY)
only_errors_log_file = normpath(config.ERRORS_ONLY_LOG_FILE)

LOGGER_CONFIGURATION = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'credentials': {
            '()': CredentialsFilter,
        },
    },
    'formatters': {
        'standard': {
            'class': 'logging.Formatter',
            'format': '%(asctime)s [%(name)-45s] [%(levelname)-8s] %(message)s',
        }
    },
    'handlers': {
        'verbose_log': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'INFO',
            'filename': join(verbose_log_folder, f'journal_{datetime.now().strftime("%d-%m-%Y_%H-%M-%S")}.log'),
            'mode': 'w',
            'formatter': 'standard',
            'maxBytes': 10485760,  # 10 MB
            'encoding': 'utf-8',
            'filters': ('credentials',),
        },
        'errors_log': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': only_errors_log_file,
            'level': 'ERROR',
            'formatter': 'standard',
            'encoding': 'utf-8',
            'maxBytes': 10485760,  # 10 MB
            'backupCount': 5,
            'filters': ('credentials',),
        },
        'stdout': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'standard',
            'stream': 'ext://sys.stdout',
            'filters': ('credentials',),
        },
    },
    'loggers': {
        '': {
            'handlers': ['verbose_log', 'errors_log', 'stdout'],
            'level': 'INFO',
        },
    }
}
