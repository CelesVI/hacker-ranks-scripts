import math
import os
import random
import re
import sys
import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    dataTime1 = datetime.datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    dataTime2 = datetime.datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    tiempo = dataTime1 - dataTime2
    absSeconds = tiempo.total_seconds()
    return round(abs(absSeconds))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(str(delta) + '\n')

    fptr.close()
