"""
  Python Logging Module example
"""

import logging
import sys
from pathlib import Path

def setup_logger(
    name: str = "jarix",
    log_file: str = "logs/jarix_experiment.log",
    console_level: int = logging.INFO,
    file_level: int = logging.DEBUG,
) -> logging.Logger:
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # Set to lowest level to capture all logs; handlers will filter
    logger.propagate = False  # prevent duplicate logs

    if logger.handlers:
        return logger  # avoid adding handlers twice

    # Ensure log directory exists
    Path(log_file).parent.mkdir(parents=True, exist_ok=True)

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(console_level)
    console_formatter = logging.Formatter("%(levelname)-8s | %(message)s")
    console_handler.setFormatter(console_formatter)

    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(file_level)
    file_formatter = logging.Formatter(
        #fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        fmt="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    file_handler.setFormatter(file_formatter)

    # Add handlers
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


if __name__ == "__main__":
    logger = setup_logger()

    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")

