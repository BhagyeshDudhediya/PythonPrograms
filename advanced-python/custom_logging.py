import logging

"""
Logger
    |_ Handler (where to log)
        |_ Formatter (what to log)
"""

format_str = '%(asctime)s:%(levelname)s:%(name)s:%(process)s:%(filename)s:%(message)s'
fmt = logging.Formatter(format_str)     # what to log

sh = logging.StreamHandler()
fh = logging.FileHandler('error.log')

# Set formatter to the handler
sh.setFormatter(fmt)
fh.setFormatter(fmt)

logger = logging.getLogger('emc')       # get logger object with name 'emc'
logger.setLevel(logging.DEBUG)

# Add handlers to logger object
# So whenever the logging is done use this logger, the logs will be dumped in these 2 handlers
# i.e on stdout and in a file named error.log
logger.addHandler(sh)
logger.addHandler(fh)

from time import sleep
if __name__ == '__main__':
    for item in range(5):
        # As logger object is configured with 2 handlers, the message will be dumped at those 2 places
        logger.debug('a dummy log content')
        sleep(0.5)

