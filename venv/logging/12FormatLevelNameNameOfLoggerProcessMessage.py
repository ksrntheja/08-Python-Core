import logging

logging.basicConfig(format='%(levelname)s:%(name)s:%(process)s:%(message)s:'
                           '%(module)s:%(lineno)s')
print('Logging Demo')
logging.debug('Debug Information')
logging.info('info Information')
logging.warning('warning Information')
logging.error('error Information')
logging.critical('critical Information')

# Logging Demo
# WARNING:root:6122:warning Information:12FormatLevelNameNameOfLoggerProcessMessage:8
# ERROR:root:6122:error Information:12FormatLevelNameNameOfLoggerProcessMessage:9
# CRITICAL:root:6122:critical Information:12FormatLevelNameNameOfLoggerProcessMessage:10
