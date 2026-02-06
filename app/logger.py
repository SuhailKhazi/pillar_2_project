import logging
import json
from datetime import datetime
from pathlib import Path

# Ensure logs folder exists
LOG_FILE = Path("data/logs.json")
LOG_FILE.parent.mkdir(exist_ok=True)

# Configure Python logging for console output
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

def log_event(event_type, data):
    """
    Logs an event to console and also appends to logs.json for audit purposes.
    Adds timestamp automatically.
    
    event_type: str, e.g., 'intake_received', 'classification_done', 'task_created'
    data: dict, any relevant information
    """
    timestamp = datetime.now().isoformat()
    log_entry = {
        "timestamp": timestamp,
        "event_type": event_type,
        "data": data
    }

    # Log to console
    logging.info(f"{event_type} | {json.dumps(data)}")

    # Append to JSON file
    try:
        if LOG_FILE.exists():
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                logs = json.load(f)
        else:
            logs = []

        logs.append(log_entry)
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            json.dump(logs, f, indent=2)
    except Exception as e:
        logging.error(f"Failed to write to log file: {e}")
