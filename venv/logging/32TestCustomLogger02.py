from CustomLogger import get_custom_logger
import logging


def logstudent():
    logger = get_custom_logger(logging.ERROR)
    logger.critical('critical message from student module')
    logger.error('error message from student module')
    logger.warning('warning message from student module')
    logger.info('info message from student module')
    logger.debug('debug message from student module')


logstudent()

#
