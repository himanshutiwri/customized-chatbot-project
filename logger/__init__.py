# logger/__init__.py
import logging
from datetime import datetime
import os

class CustomLogger:
    """Custom logger class for the application."""

    def __init__(self):
        # Directory for log files
        self.log_dir = "logs"
        os.makedirs(self.log_dir, exist_ok=True)  # Ensure the directory exists

        # Timestamped log file
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        log_file = os.path.join(self.log_dir, f"app_{timestamp}.log")

        # Configure logging
        logging.basicConfig(
            filename=log_file,
            filemode="w",
            format="[%(asctime)s] %(levelname)s - %(message)s",
            level=logging.INFO
        )
        self.logger = logging.getLogger(__name__)

    def get_logger(self):
        """Return the configured logger."""
        return self.logger  