#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    stair = []
    for _pass in range(1, n + 1):
        step = ' ' * (n - _pass) + '#' * _pass
        print(step)
        stair.append(step)
    return stair

def staircase_optimized(n):
    for _ in range(1, n + 1):
        print(' ' * (n - _) + '#' * _)

if __name__ == '__main__':
    n = int(input())

    staircase(n)
