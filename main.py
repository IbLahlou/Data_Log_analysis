import time
import os
import random
from datetime import datetime

spool_dir = "/root/big_Data/Data_Log_analysis/spool"
log_file = os.path.join(spool_dir, "log.log")

def simulate_log():
    log_levels = ['INFO', 'ERROR', 'WARNING']
    log_sources = ['source_A', 'source_B', 'source_C']
    
    timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    log_level = random.choice(log_levels)
    log_source = random.choice(log_sources)
    log_message = f"Log message generated from {log_source} - {log_level} - {timestamp}"
    
    return log_message

def write_to_log_file(log_data):
    with open(log_file, "a") as file:
        file.write(log_data + "\n")

def simulate_log_stream():
    while True:
        log_message = simulate_log()
        write_to_log_file(log_message)
        print(log_message)
        time.sleep(random.uniform(1, 5))

if __name__ == "__main__":
    simulate_log_stream()
