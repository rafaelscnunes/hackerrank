#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    """:return the sum of all the numbers in the ar array as integer

    :param ar: list() of items
    :return: int() with the sum of all numbers
    """

    _sum = 0
    for item in ar:
        try:
            _sum += item
        except:
            pass
    return int(_sum)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
