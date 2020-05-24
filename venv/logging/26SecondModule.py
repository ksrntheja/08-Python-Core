import logging
import TestCustom

logger = logging.getLogger('secondlogger')
logger.setLevel(logging.DEBUG)

fileHandler = logging.FileHandler('secondlogger.log', mode='a')

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                              datefmt='%d/%m/%Y %I:%M:%S %p')

fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)

logger.debug('Debug Information-secondlogger')
logger.info('info Information-secondlogger')
logger.warning('warning Information-secondlogger')
logger.error('error Information-secondlogger')
logger.critical('critical Information-secondlogger')

# ERROR: error Information
# CRITICAL: critical Information
