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

def main():
    total_size = 0
    status_counts = {code: 0 for code in VALID_STATUS_CODES}
    line_count = 0
    
    def signal_handler(sig, frame):
        print_statistics(total_size, status_counts)
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)
    
    for line in sys.stdin:
        try:
            parts = line.split()
            if len(parts) >= 7:
                status_code = int(parts[-2])
                file_size = int(parts[-1])
                
                if status_code in VALID_STATUS_CODES:
                    total_size += file_size
                    status_counts[status_code] += 1
                    
                    line_count += 1
                    if line_count % 10 == 0:
                        print_statistics(total_size, status_counts)
            
        except ValueError:
            # If conversion to int fails, skip the line
            continue
    
    print_statistics(total_size, status_counts)

if __name__ == "__main__":
    main()

