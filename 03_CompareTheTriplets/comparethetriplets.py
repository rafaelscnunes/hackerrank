#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    """Return a list with the scores

        Generated by comparing the first and the second triple
        If the comparision between correspondent numbers result
        in a greater one this one score's is incremented by 1,
        if the correspondent numbers are equal nothing is added
        to the score

    :param a: first triple
    :param b: second triple
    :return: list() [first_score, second_score]
    """

    first_score, second_score = 0, 0
    for first, second in zip(a, b):
        if int(first) > int(second):
            first_score += 1
        if int(second) > int(first):
            second_score += 1
    return [first_score, second_score]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

