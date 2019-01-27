'''
Question: Left Rotation
https://www.hackerrank.com/challenges/array-left-rotation/problem?h_r=next-challenge&h_v=zen

'''

#!/bin/python3

import math
import os
import random
import re
import sys

def leftRotation(rotationNum, targetLst):
    targetLstLength = len(targetLst)
    res = targetLst[rotationNum:] + targetLst[0:rotationNum]
    print(' '.join([str(element) for element in res]))


if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    leftRotation(d, a)

    