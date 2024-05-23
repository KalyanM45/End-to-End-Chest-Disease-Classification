import os
import logging
from datetime import datetime

log_dir = 'Logs'
date_subdir = datetime.now().strftime('%d_%m_%Y')
LOG_FILE = datetime.now().strftime('%H_%M_%S - %d_%m_%Y.log')
logs_path = os.path.join(os.getcwd(), log_dir, date_subdir, LOG_FILE)

os.makedirs(os.path.join(os.getcwd(), log_dir, date_subdir), exist_ok=True)

logging.basicConfig(
    filename = logs_path,
    format = "[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level = logging.DEBUG
    )