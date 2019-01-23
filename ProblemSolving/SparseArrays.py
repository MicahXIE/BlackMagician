'''
Question: Sparse Arrays
https://www.hackerrank.com/challenges/sparse-arrays/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    res = []
    stringDict = {}
    for stringItem in strings:
        if stringItem in stringDict:
            stringDict[stringItem] += 1
        else:
            stringDict[stringItem] = 1
    
    for queryItem in queries:
        if queryItem in stringDict:
            res.append(stringDict[queryItem])
        else:
            res.append(0)

    return res    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
