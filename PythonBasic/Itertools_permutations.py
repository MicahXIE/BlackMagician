'''
example:
>>> from itertools import permutations
>>> print permutations(['1','2','3'])
<itertools.permutations object at 0x02A45210>
>>> 
>>> print list(permutations(['1','2','3']))
[('1', '2', '3'), ('1', '3', '2'), ('2', '1', '3'), ('2', '3', '1'), ('3', '1', '2'), ('3', '2', '1')]
>>> 
>>> print list(permutations(['1','2','3'],2))
[('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
>>>
>>> print list(permutations('abc',3))
[('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]

Sample Input:
HACK 2

Sample Output:
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
'''

from itertools import permutations

if __name__ == "__main__":
    s, n = input().split()
    n = int(n)
    lst = list(permutations(s, n))
    res = []
    for t in lst:
        res.append(''.join(t))
    
    res.sort()
    
    for s in res:
        print(s)

