import logging

logger = logging.getLogger('testlogger')
logger.setLevel(logging.DEBUG)

fileHandler = logging.FileHandler('testlogger.log', mode='w')
fileHandler.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')

fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)

logger.debug('Debug Information-testlogger')
logger.info('info Information-testlogger')
logger.warning('warning Information-testlogger')
logger.error('error Information-testlogger')
logger.critical('critical Information-testlogger')

#
