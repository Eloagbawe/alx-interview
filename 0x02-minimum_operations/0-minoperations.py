#!/usr/bin/python3
"""This file contains the minOperations function"""


def minOperations(n):
    """This calculates the fewest number of
    operations needed to result in exactly n H
    characters in a file"""
    if (isinstance(n, int) and (n > 0)):
        operations = 0
        string = 1
        latest_copy = 0

        while string < n:
            if latest_copy == 0:
                latest_copy = string
                operations += 1
            if string == 1:
                string += latest_copy
                operations += 1
                continue
            target = n - string
            if target < latest_copy:
                return 0
            if target % string != 0:
                string += latest_copy
                operations += 1
            else:
                latest_copy = string
                string += latest_copy
                operations += 2
        if string == n:
            return operations
        else:
            return 0
    return 0
