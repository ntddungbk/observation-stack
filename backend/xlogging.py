import logging
from logging.handlers import RotatingFileHandler


class Logger:
    app_name: str = "test-app"

    def __init__(self):
        # get logger instance from logging module with app_name
        self.logger = logging.getLogger(self.app_name)
        self.logger.setLevel(logging.INFO)

        # if logger has no handlers, add a stream handler
        if not self.logger.handlers:
            log_handler = RotatingFileHandler(
                "logs/app.log", backupCount=5
            )  # Specify your log file name
            log_handler.setLevel(logging.INFO)
            formatter = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            log_handler.setFormatter(logging.Formatter(formatter))
            self.logger.addHandler(log_handler)

    def debug(self, msg, *args, **kwargs):
        self.logger.debug(msg, *args, stacklevel=2)

    def warning(self, msg, *args, **kwargs):
        self.logger.warning(msg, *args, stacklevel=2)

    def error(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, stacklevel=2)

    def info(self, msg, *args, **kwargs):
        self.logger.info(msg, *args, stacklevel=2)

    def exception(self, msg, *args, **kwargs):
        self.logger.exception(msg, *args, stacklevel=2)
