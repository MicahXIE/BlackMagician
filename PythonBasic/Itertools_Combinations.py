'''
Sample Input

HACK 2
Sample Output

A
C
H
K
AC
AH
AK
CH
CK
HK
'''

from itertools import combinations

s,k = input().strip().split()
k = int(k)
s = ''.join(sorted(s))
for i in range(1,k+1):
    lst = list(combinations(s,i))
    for item in lst:
        print(''.join(item))

