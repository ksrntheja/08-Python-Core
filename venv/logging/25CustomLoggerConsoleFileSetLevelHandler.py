import logging

logger = logging.getLogger('demologger')
logger.setLevel(logging.DEBUG)

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.ERROR)
fileHandler = logging.FileHandler('customlog.log', mode='w')

formatter01 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                datefmt='%d/%m/%Y %I:%M:%S %p')

formatter02 = logging.Formatter('%(levelname)s: %(message)s')

consoleHandler.setFormatter(formatter02)
fileHandler.setFormatter(formatter01)

logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)

logger.debug('Debug Information')
logger.info('info Information')
logger.warning('warning Information')
logger.error('error Information')
logger.critical('critical Information')

# ERROR: error Information
# CRITICAL: critical Information
