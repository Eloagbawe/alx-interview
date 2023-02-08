#!/usr/bin/python3
"""This file contains the minOperations function"""


def minOperations(n):
    """This calculates the fewest number of
    operations needed to result in exactly n H
    characters in a file"""
    if (n > 0):
        operations = 0
        string = 'H'
        latest_copy = ''

        while len(string) < n:
            if (n % len(string) == 0):
                string += string
                latest_copy = string
                operations += 2
            else:
                string += latest_copy
                operations += 1
        return operations
    return 0
