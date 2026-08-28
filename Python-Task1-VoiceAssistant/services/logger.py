import logging
import os


# =========================================================
# LOG DIRECTORY
# =========================================================

LOG_DIR = "logs"

os.makedirs(LOG_DIR, exist_ok=True)


# =========================================================
# LOG FILE
# =========================================================

LOG_FILE = os.path.join(
    LOG_DIR,
    "assistant.log"
)


# =========================================================
# LOGGER CONFIGURATION
# =========================================================

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format=(
        "%(asctime)s - "
        "%(levelname)s - "
        "%(message)s"
    )
)


# =========================================================
# LOGGER OBJECT
# =========================================================

logger = logging.getLogger("voice_assistant")