import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    # initial level of logging and format
    level= logging.INFO,
    format= logging_str,

    handlers=[
        # creates a log folder and saves the log file in that folder
        logging.FileHandler(log_filepath),
        # prints the log in the terminal
        logging.StreamHandler(sys.stdout)
    ]
)

# initialize logging in your project
logger = logging.getLogger("mlProjectLogger")