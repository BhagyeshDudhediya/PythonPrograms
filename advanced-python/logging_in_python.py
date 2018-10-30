"""logging is python module to log the events occurring
logging is thread/process safe, only one thread will invokde it at a time.
It is better to use logging in multi threading areas as print is not thread safe
and hence multiple threads can call print at a same time"""
import logging  # by default creates a root logger

format_str = '%(asctime)s:%(levelname)s:%(name)s:%(process)s:%(filename)s:%(message)s'
# Customise logging level to use proper format, and also dump logs into a file
# To dump different types of logs in different files, you need to create different
# logger objects with different filename flag

logging.basicConfig(level=logging.DEBUG, format=format_str, filename='access.log')    # without this debug and info will not be displayed
logging.debug("debug messages")             # Least priority
logging.info("confirmation note")
logging.warning("warning message")
logging.error("an error information")
logging.critical("a critical message")      # Most priority