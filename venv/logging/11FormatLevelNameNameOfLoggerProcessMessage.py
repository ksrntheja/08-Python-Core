import logging

logging.basicConfig(format='%(levelname)s:%(name)s:%(process)s:%(message)s')
print('Logging Demo')
logging.debug('Debug Information')
logging.info('info Information')
logging.warning('warning Information')
logging.error('error Information')
logging.critical('critical Information')

# WARNING:root:6095:warning Information
# ERROR:root:6095:error Information
# CRITICAL:root:6095:critical Information
# Logging Demo
