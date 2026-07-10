import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

# ------------------------------------------------------------------
# Create logs directory
# ------------------------------------------------------------------

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "app.log"


def get_logger(name: str) -> logging.Logger:
    """
    Return a configured logger instance.
    """

    logger = logging.getLogger(name) # logger instance is created with the specified name. This allows for different parts of the application to have their own loggers, which can be configured independently.

    logger.setLevel(logging.INFO) # The logger's level is set to INFO, meaning it will capture all messages at this level and above (e.g., WARNING, ERROR, CRITICAL).

    if not logger.handlers:

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(funcName)s | %(message)s"
        )
        # The formatter is defined to specify the format of log messages. It includes the timestamp, log level, logger name, function name, and the actual log message.

        # Console Handler , which outputs log messages to the console (standard output). This is useful for development and debugging.
        console_handler = logging.StreamHandler() 
        console_handler.setFormatter(formatter)

        # Rotating File Handler
        file_handler = RotatingFileHandler(
            LOG_FILE,
            maxBytes=10 * 1024 * 1024,   # 10 MB
            backupCount=5, # Keep 5 backup files, means after 5 files, the oldest will be deleted
            encoding="utf-8"
        )

        # file_handler is configured to write log messages to a file, with rotation based on size. When the log file reaches 10 MB, it will be rotated, and up to 5 backup files will be kept. This prevents the log file from growing indefinitely and consuming too much disk space.
        file_handler.setFormatter(formatter)

        logger.addHandler(console_handler) # The console handler is added to the logger, so log messages will be printed to the console.

        logger.addHandler(file_handler) # The file handler is added to the logger, so log messages will also be written to the specified log file.

    return logger