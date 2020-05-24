import logging
import logging.config

logging.config.fileConfig("37logging_config_console.init")

logger = logging.getLogger('demologger')
logger.critical('It is critical message')
logger.error('It is error message')
logger.warning('It is warning message')
logger.info('It is info message')
logger.debug('It is debug message')

# 24/05/2020 01:09:42 PM:demologger:CRITICAL:It is critical message
# 24/05/2020 01:09:42 PM:demologger:ERROR:It is error message
# 24/05/2020 01:09:42 PM:demologger:WARNING:It is warning message
