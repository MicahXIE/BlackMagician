
'''
Question: Dynamic Array
https://www.hackerrank.com/challenges/dynamic-array/problem

'''

#!/bin/python3

import math
import os
import random
import re
import sys

QUERY_ONE = 1
QUERY_TWO = 2

# Complete the dynamicArray function below.
def dynamicArray(n, queries):

    seqLst = [[] for _ in range(n)]
    #seqLst = [[]] * n
    lastAnswer = 0
    res = []

    for queryItem in queries:
        queryType = queryItem[0]
        x = queryItem[1]
        y = queryItem[2]

        seqIndex = (x^lastAnswer)%n
        if queryType == QUERY_ONE:
            seqLst[seqIndex].append(y)
        
        if queryType == QUERY_TWO:
            currentSeqSize = len(seqLst[seqIndex])
            lastAnswer = seqLst[seqIndex][y%currentSeqSize]
            res.append(lastAnswer)
    
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().rstrip().split()

    n = int(nq[0])

    q = int(nq[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

