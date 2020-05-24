import logging

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s')
print('Logging Demo')
logging.debug('Debug Information')
logging.info('info Information')
logging.warning('warning Information')
logging.error('error Information')
logging.critical('critical Information')

# Logging Demo
# 2020-05-23 21:59:50,269:WARNING:warning Information
# 2020-05-23 21:59:50,269:ERROR:error Information
# 2020-05-23 21:59:50,269:CRITICAL:critical Information
