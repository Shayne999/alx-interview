#!/usr/bin/env python3
import sys
import signal

# Define valid status codes
VALID_STATUS_CODES = {200, 301, 400, 401, 403, 404, 405, 500}

def print_statistics(total_size, status_counts):
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        if status_code in VALID_STATUS_CODES:
            print(f"{status_code}: {status_counts[status_code]}")
