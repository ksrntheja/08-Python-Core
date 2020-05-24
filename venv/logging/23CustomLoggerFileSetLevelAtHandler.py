import logging

logger = logging.getLogger('demologger')
logger.setLevel(logging.INFO)

fileHandler = logging.FileHandler('customlog.log', mode='w')
fileHandler.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                              datefmt='%d/%m/%Y %I:%M:%S %p')

fileHandler.setFormatter(formatter)

logger.addHandler(fileHandler)

logger.debug('Debug Information')
logger.info('info Information')
logger.warning('warning Information')
logger.error('error Information')
logger.critical('critical Information')
