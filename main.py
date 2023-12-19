import time
import os
import random
from datetime import datetime

spool_dir = "./spool"
log_file = os.path.join(spool_dir, "log.txt")

log_levels = ["INFO", "WARNING", "ERROR"]

def write_to_log_file(log_data):
    with open(log_file, "a") as file:
        file.write(log_data + "\n")

def detect_anomalies(log_message):
    if "ERROR" in log_message or "WARNING" in log_message:
        print(f"Anomaly detected: {log_message}")
        # Add your custom action for handling anomalies here

def generate_log_message():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_level = random.choice(log_levels)
    return f"{timestamp} - Level {log_level}: This is a {log_level} log message."

def simulate_log_stream():
    while True:
        log_message = generate_log_message()
        write_to_log_file(log_message)
        detect_anomalies(log_message)
        time.sleep(random.uniform(1, 5))

if __name__ == "__main__":
    simulate_log_stream()
