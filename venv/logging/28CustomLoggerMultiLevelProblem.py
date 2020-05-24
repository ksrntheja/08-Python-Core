import logging

logger = logging.getLogger('demologger')
logger.setLevel(logging.INFO)

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                              datefmt='%d/%m/%Y %I:%M:%S %p')

consoleHandler.setFormatter(formatter)

logger.addHandler(consoleHandler)

logger.debug('Debug Information')
logger.info('info Information')
logger.warning('warning Information')
logger.error('error Information')
logger.critical('critical Information')

# 23/05/2020 11:19:15 PM - demologger - INFO: info Information
# 23/05/2020 11:19:15 PM - demologger - WARNING: warning Information
# 23/05/2020 11:19:15 PM - demologger - ERROR: error Information
# 23/05/2020 11:19:15 PM - demologger - CRITICAL: critical Information
