'''
topic details:
https://www.hackerrank.com/challenges/python-sort-sort/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

Sample Input 0

5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1   --- K
Sample Output 0

7 1 0
10 2 5
6 5 9
9 9 9
1 23 12

Explanation 0

The details are sorted based on the second attribute, since K is zero-indexed.
'''
#!/bin/python3

import math
import os
import random
import re
import sys
from operator import itemgetter



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    #res = sorted(arr, key=itemgetter(k))
    res = sorted(arr, key=lambda l:l[k])
    
    for item in res:
        print(' '.join(str(x) for x in item))

