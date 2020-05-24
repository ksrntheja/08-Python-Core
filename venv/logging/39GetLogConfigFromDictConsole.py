import logging
from logging.config import dictConfig

logging_config = dict(
    version=1,
    formatters={
        'f': {
            'format': '%(asctime)s:%(name)s:%(levelname)s:%(message)s',
            'datefmt': '%d/%m/%Y %I:%M:%S %p'
        }
    },
    handlers={
        'h': {
            'class': 'logging.StreamHandler',
            'formatter': 'f',
            'level': logging.DEBUG
        }
    },
    root={
        'handlers': ['h'],
        'level': logging.DEBUG,
    },
)
dictConfig(logging_config)

logger = logging.getLogger()
logger.critical('it is critical message')
logger.error('it is error message')
logger.warning('it is warning message')
logger.info('it is info message')
logger.debug('it is debug message')

print('type(logging_config)', type(logging_config))
print("type(logging_config['version'])", type(logging_config['version']))
print("type(logging_config['formatters'])", type(logging_config['formatters']))
print("type(logging_config['formatters']['f'])", type(logging_config['formatters']['f']))
print("type(logging_config['formatters']['f']['format'])", type(logging_config['formatters']['f']['format']))

# 24/05/2020 01:18:17 PM:root:CRITICAL:it is critical message
# 24/05/2020 01:18:17 PM:root:ERROR:it is error message
# 24/05/2020 01:18:17 PM:root:WARNING:it is warning message
# 24/05/2020 01:18:17 PM:root:INFO:it is info message
# 24/05/2020 01:18:17 PM:root:DEBUG:it is debug message
# type(logging_config) <class 'dict'>
# type(logging_config['version']) <class 'int'>
# type(logging_config['formatters']) <class 'dict'>
# type(logging_config['formatters']['f']) <class 'dict'>
# type(logging_config['formatters']['f']['format']) <class 'str'>
