'''
Sample Input:
7 3
Tsi
h%x
i #
sM 
$a 
#t%
ir!

Sample Output:
This is Matrix#  %!

Zip usage:
>>>a = [1,2,3]
>>> b = [4,5,6]
>>> zipped = zip(a,b)     # 打包为元组的列表
[(1, 4), (2, 5), (3, 6)]

to be updated for summary of re package usage

'''

import math
import os
import random
import re
import sys


nm = input().split()

n = int(nm[0])

m = int(nm[1])

matrix = []

for _ in range(n):
    matrix_item = input().replace('\r', '')
    matrix.append(matrix_item)
    
res = ''
for s in zip(*matrix):
    res += ''.join(s)

print(re.sub(r'(?<=\w)([^\w]+)(?=\w)', r' ', res))