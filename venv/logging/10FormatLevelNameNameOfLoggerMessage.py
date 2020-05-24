import logging

logging.basicConfig(format='%(levelname)s:%(name)s:%(message)s')
print('Logging Demo')
logging.debug('Debug Information')
logging.info('info Information')
logging.warning('warning Information')
logging.error('error Information')
logging.critical('critical Information')

# Logging Demo
# WARNING:root:warning Information
# ERROR:root:error Information
# CRITICAL:root:critical Information
