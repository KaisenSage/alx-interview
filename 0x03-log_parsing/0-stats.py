#!/usr/bin/python3
import sys
import signal
import re

# Initialize variables
total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

# Regular expression to parse log lines
log_pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+) - \[.*?\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)')

def print_stats():
    """Print the current statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

def signal_handler(sig, frame):
    """Handle signal interrupt."""
    print_stats()
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1
        match = log_pattern.match(line)
        if match:
            status_code = int(match.group(2))
            file_size = int(match.group(3))
            total_size += file_size
            if status_code in status_counts:
                status_counts[status_code] += 1
        
        if line_count % 10 == 0:
            print_stats()

    # Print the final stats
    print_stats()

except Exception as e:
    pass

