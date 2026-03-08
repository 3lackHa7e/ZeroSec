import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Create a logger
logger = logging.getLogger(__name__)

# Example log messages
logger.info('Logging module initialized')

# You can use logger methods for different log levels
# logger.debug('Debug message')
# logger.warning('Warning message')
# logger.error('Error message')
# logger.critical('Critical message')