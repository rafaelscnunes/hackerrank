#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    timestrs = s.split(':')
    hour = timestrs[0]
    minute = timestrs[1]
    second = timestrs[2][:2]
    am_pm = timestrs[2][2:].upper()

    if am_pm == 'PM':
        if hour < '12':
            hour = str(int(hour) + 12)
    elif hour == '12':
        hour = '00'

    return '{0}:{1}:{2}'.format(hour, minute, second)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
