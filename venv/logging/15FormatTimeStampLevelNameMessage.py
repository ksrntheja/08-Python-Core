import logging

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S')
print('Logging Demo')
logging.debug('Debug Information')
logging.info('info Information')
logging.warning('warning Information')
logging.error('error Information')
logging.critical('critical Information')

# Logging Demo
# 23/05/2020 22:03:45:WARNING:warning Information
# 23/05/2020 22:03:45:ERROR:error Information
# 23/05/2020 22:03:45:CRITICAL:critical Information
