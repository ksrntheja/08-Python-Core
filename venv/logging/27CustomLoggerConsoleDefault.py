import logging

logger = logging.getLogger('demologger')

consoleHandler = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                              datefmt='%d/%m/%Y %I:%M:%S %p')

consoleHandler.setFormatter(formatter)

logger.addHandler(consoleHandler)

logger.debug('Debug Information')
logger.info('info Information')
logger.warning('warning Information')
logger.error('error Information')
logger.critical('critical Information')

# 23/05/2020 11:15:57 PM - demologger - WARNING: warning Information
# 23/05/2020 11:15:57 PM - demologger - ERROR: error Information
# 23/05/2020 11:15:57 PM - demologger - CRITICAL: critical Information