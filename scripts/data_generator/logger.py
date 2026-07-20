import logging
from pathlib import Path

from config.settings import LOG_DIR


def setup_logger(name: str) -> logging.Logger:
    """
    Create and configure a logger.

    Parameters
    -----------
    name : str
       Logger name.


    Returns
    --------
    logging.Logger
    """
    LOG_DIR.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger(name)

    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler = logging.FileHandler(LOG_DIR / "etl.log", encoding="utf-8")

    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
