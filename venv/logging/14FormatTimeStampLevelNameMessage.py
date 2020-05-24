import logging

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S%p')
print('Logging Demo')
logging.debug('Debug Information')
logging.info('info Information')
logging.warning('warning Information')
logging.error('error Information')
logging.critical('critical Information')

# 23/05/2020 11:12:35PM:WARNING:warning Information
# 23/05/2020 11:12:35PM:ERROR:error Information
# 23/05/2020 11:12:35PM:CRITICAL:critical Information
# Logging Demo
