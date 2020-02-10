#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    candles = {}
    biggest = 0
    for size in ar:
        if size not in candles:
            candles[size] = 1
        else:
            candles[size] += 1
        if size > biggest:
            biggest = size
    return candles[biggest]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
