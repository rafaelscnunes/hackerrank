#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr, precision='{:.6f}'):
    negative, positive, zero = 0, 0, 0
    for item in arr:
        if item < 0:
            negative += 1
        elif item > 0:
            positive += 1
        else:
            zero += 1
    length = len(arr)
    print(precision.format(positive / length))
    print(precision.format(negative / length))
    print(precision.format(zero / length))
    return [precision.format(positive / length),
            precision.format(negative / length),
            precision.format(zero / length)]


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
