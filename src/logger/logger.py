import os
import logging
import sys


class Logger:

    def __init__(self, log_level: int, log_path: str) -> None:
        """
        :param log_level: one of DEBUG, INFO, WARNING, ERROR, CRITICAL, FATAL
        :param log_path: path to .log file
        """
        logging.basicConfig(level=log_level,
                            format="%(asctime)s %(levelname)s %(message)s",
                            datefmt="%Y-%m-%d %H:%M:%S",
                            filename=log_path)

    @staticmethod
    def log_info(message: str) -> None:
        file = sys._getframe(1).f_code.co_filename
        func = sys._getframe(1).f_code.co_name
        line = sys._getframe(1).f_code.co_firstlineno
        log_str = f"{file} {line} {func} {message}"
        logging.info(log_str)


log_levels = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL,
    "FATAL": logging.FATAL
}


log_level = os.environ.get("LOG_LEVEL", "INFO")
log_level = log_levels.get(log_level, logging.WARNING)
log_path = os.environ.get("LOG_PATH", "logs.log")
log = Logger(log_level, log_path=log_path)
