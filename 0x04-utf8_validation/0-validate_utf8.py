#!/usr/bin/python3
""" 0-validate_utf8 module """


def validUTF8(data):
    """ method that determines if a given data set
    represents a valid UTF-8 encoding
    Args:
        data (list): data to be valdated
    Return:
        bool: True if valid, false if invlid
    """
    num_bytes = 0

    for byte in data:
        if byte < 0 or byte > 255:
            return False

        if num_bytes == 0:
            if (byte >> 5) == 0x06:
                num_bytes = 1
            elif (byte >> 4) == 0x0E:
                num_bytes = 2
            elif (byte >> 3) == 0x1E:
                num_bytes = 3
            elif (byte >> 7) != 0x00:
                return False
        else:
            if (byte >> 6) != 0x02:
                return False
            num_bytes -= 1

    return num_bytes == 0
