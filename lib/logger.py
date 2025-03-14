import logging
import os


class Logger:
    def __init__(self, log_dir="logs", log_file="app.log"):
        """Initializes the logger with console and file handlers."""
        os.makedirs(log_dir, exist_ok=True)  # Ensure the log directory exists

        log_path = os.path.join(log_dir, log_file)

        # Configure logging
        logging.basicConfig(
            level=logging.INFO,  # Adjust level as needed (DEBUG, WARNING, ERROR, etc.)
            format="%(asctime)s %(levelname)s %(name)s: %(message)s",
            handlers=[
                logging.StreamHandler(),  # Log to console
                logging.FileHandler(log_path, mode="a")  # Log to file
            ]
        )

        self.logger = logging.getLogger("python_app")

    def info(self, msg):
        self.logger.info(msg)

    def error(self, msg):
        self.logger.error(msg)


# Initialize the logger
logger = Logger()
