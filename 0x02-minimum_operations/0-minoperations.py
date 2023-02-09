#!/usr/bin/python3
"""This file contains the minOperations function"""


def minOperations(n):
    """This calculates the fewest number of
    operations needed to result in exactly n H
    characters in a file"""
    if (isinstance(n, int) and (n > 0)):
        operations = 0
        string = 'H'
        latest_copy = ''

        while len(string) < n:
            if ((len(string) == 1) and (len(latest_copy) == 0)):
                latest_copy = 'H'
                string += latest_copy
                operations += 2
                continue
            if (n % len(string) == 0):
                latest_copy = string
                string += latest_copy
                operations += 2
            else:
                string += latest_copy
                operations += 1
        if (len(string) == n):
            return operations
        else:
            return 0
    return 0
