#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr = sorted(arr)
    minimum, maximum = 0, 0
    for index in range(len(arr) - 1):
        minimum += arr[index]
        maximum += arr[index + 1]
    print('{0} {1}'.format(minimum, maximum))
    return [minimum, maximum]


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
