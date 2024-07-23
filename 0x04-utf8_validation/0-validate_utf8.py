#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """Function that checks if a given data set
    represents a valid UTF-8 encoding
    """
    num_bytes = 0
    msb = 1 << 7
    msb2 = 1 << 6

    for byte in data:
        byte = byte & 0xFF

        if num_bytes == 0:
            msb = 1 << 7

            while msb & byte:
                num_bytes += 1
                msb = msb >> 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False

        else:
            if not (byte & msb and not (byte & msb2)):
                return False

        num_bytes -= 1

    return num_bytes == 0
