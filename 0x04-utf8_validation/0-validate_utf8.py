#!/usr/bin/python3
"""This file contains the validUTF8 function"""


def validUTF8(data):
    """This function determines if a given data set
    represents a valid UTF-8 encoding
    """
    # Initialize a variable to keep track of the number of continuation bytes
    num_continuation_bytes = 0

    # Iterate through each byte in the data
    for byte in data:
        # Check if the byte is a continuation byte
        if num_continuation_bytes > 0 and (byte >> 6) == 0b10:
            # If it is a continuation byte, decrement the number
            # of continuation bytes
            num_continuation_bytes -= 1
        # Otherwise, check if the byte is the start of a multi-byte sequence
        elif num_continuation_bytes == 0:
            if (byte >> 7) == 0:
                # If the byte starts with a 0, it is a single-byte character
                num_continuation_bytes = 0
            elif (byte >> 5) == 0b110:
                # If the byte starts with 110, it is a two-byte character
                num_continuation_bytes = 1
            elif (byte >> 4) == 0b1110:
                # If the byte starts with 1110, it is a three-byte character
                num_continuation_bytes = 2
            elif (byte >> 3) == 0b11110:
                # If the byte starts with 11110, it is a four-byte character
                num_continuation_bytes = 3
            else:
                # If the byte does not match any of the above patterns,
                # it is not a valid UTF-8 character
                return False
        else:
            # If the byte is not a continuation byte and not the start of a
            # multi-byte sequence, it is not a valid UTF-8 character
            return False

    # If we have iterated through all the bytes without returning False,
    # the data is a valid UTF-8 encoding
    return num_continuation_bytes == 0
