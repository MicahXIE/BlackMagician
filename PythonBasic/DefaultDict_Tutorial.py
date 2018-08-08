'''
topic: https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

Sample Input

5 2
a
a
b
a
b
a
b
Sample Output

1 2 4
3 5
'''

'''
Below is the wrong answer:

from collections import defaultdict

if __name__ == '__main__':
    n,m = map(int, input().strip().split())
    
    A = []
    for _ in range(n):
        A.append(input().strip())
    
    B = []
    for _ in range(m):
        B.append(input().strip())
    
    # key issue is below, the dict should store all the keys from A
    d = defaultdict(list)
    for k in B:
        for i in range(n):
            if A[i] == k:
                d[k].append(str(i+1))
    
    for k in B:
        if k in d.keys():
            print(' '.join(d[k]))
        else:
            print('-1')
'''

from collections import defaultdict

if __name__ == '__main__':
    n,m = map(int, input().strip().split())
    d = defaultdict(list)
    
    for i in range(1,n+1):
        d[input().strip()].append(str(i))
    
    for k in range(m):
        print(' '.join(d[input().strip()]) or -1)