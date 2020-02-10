#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the winner function below.
first = 'Manasa'
second = 'Sandy'

def turn(A):
    S = (13, 11, 7, 5, 3, 2)
    for bucket in range(len(A)):
        for s in S:
            if (A[bucket] - s) == 0:
                A[bucket] = 0
                return True, A
    for index in range(len(S)):
        for bucket in range(len(A)):
            if S[index] <= A[bucket]:
                A[bucket] -= S[index]
                return True, A
    return False, A

def exchange(player):
    if player == first:
        return second
    else:
        return first

def winner(A):
    A = sorted(A, reverse=True)
    print(A)
    player = first
    while True:
        played, A = turn(A)
        print(player, played, A)
        player = exchange(player)
        if not played:
            print(player)
            return player


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        A = list(map(int, input().rstrip().split()))

        result = winner(A)

        fptr.write(result + '\n')

    fptr.close()
