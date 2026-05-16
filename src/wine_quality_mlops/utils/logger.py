import logging
import os
import sys
from datetime import datetime
from pathlib import Path

LOG_DIR = "logs"
Path(LOG_DIR).mkdir(exist_ok=True)

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# LOG_FORMAT = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
LOG_FORMAT = (
    "[%(asctime)s] "
    "%(filename)s:%(lineno)d "
    "%(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger("datascienceLogger")
logger.setLevel(logging.INFO)

if not logger.handlers:

    file_handler = logging.FileHandler(LOG_FILE_PATH)
    console_handler = logging.StreamHandler(sys.stdout)

    formatter = logging.Formatter(LOG_FORMAT)

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)