import logging

logging.basicConfig(filename='log02.txt', level=logging.DEBUG, filemode='w')
import Test

print('Logging Demo')
logging.debug('Debug Information')
logging.info('info Information')
logging.warning('warning Information')
logging.error('error Information')
logging.critical('critical Information')

# Logging Demo-Test
# Logging Demo
