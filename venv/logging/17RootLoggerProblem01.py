import logging

logging.basicConfig(filename='log01.txt', level=logging.DEBUG, filemode='w')
logging.basicConfig(filename='log02.txt', level=logging.ERROR, filemode='w')
print('Logging Demo')
logging.debug('Debug Information')
logging.info('info Information')
logging.warning('warning Information')
logging.error('error Information')
logging.critical('critical Information')

# Logging Demo
