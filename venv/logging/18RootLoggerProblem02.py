import logging
import Test

logging.basicConfig(filename='log02.txt', level=logging.DEBUG, filemode='w')
print('Logging Demo')
logging.debug('Debug Information')
logging.info('info Information')
logging.warning('warning Information')
logging.error('error Information')
logging.critical('critical Information')

# Logging Demo-Test
# Logging Demo
# WARNING:root:warning Information-Test
# ERROR:root:error Information-Test
# CRITICAL:root:critical Information-Test
# WARNING:root:warning Information
# ERROR:root:error Information
# CRITICAL:root:critical Information
