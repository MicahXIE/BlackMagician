'''
Question: Array Manipulation
https://www.hackerrank.com/challenges/crush/problem

Sample Input:
5 3
1 2 100
2 5 100
3 4 100

Sample Output:
[100, 0, -100, 0, 0]
[100, 100, -100, 0, 0]
[100, 100, 0, 0, -100]

___    
   |___

'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    targetLst = [0]*n
    for queryItem in queries:
        a = queryItem[0]
        b = queryItem[1]
        k = queryItem[2]

        # add the sum to (a-1), minus the sum for the element after (b-1)
        targetLst[a-1] += k
        if (b<=(n-1)):
            targetLst[b] -= k

        print(targetLst)    

    targetLstMax = 0
    targetLstSum = 0
    for targetLstItem in targetLst:
        targetLstSum += targetLstItem

        if targetLstSum > targetLstMax:
            targetLstMax = targetLstSum
    
    return targetLstMax



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()


