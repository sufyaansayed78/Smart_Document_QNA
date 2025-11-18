import os 
import logging
from datetime import datetime
log_files = "LOGS"
os.makedirs(log_files, exist_ok=True)
from datetime import datetime

log_file = f"LOG AT - {datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.log"
log_path = os.path.join(log_files, log_file)
logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format="[%(asctime)s]:%(levelname)s]:%(message)s:"
) 
logging.info("Logging has started")
logger = logging.getLogger()
