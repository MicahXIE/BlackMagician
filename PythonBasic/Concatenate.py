
'''
Sample Input

4 3 2
1 2
1 2 
1 2
1 2
3 4
3 4
3 4 
Sample Output

[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]] 

'''

import numpy

m,n,p= map(int, input().strip().split())
m_lst = []
n_lst = []

for _ in range(m):
    m_lst.append(list(map(int, input().strip().split())))

m_array = numpy.array(m_lst)

for _ in range(n):
    n_lst.append(list(map(int, input().strip().split())))

n_array = numpy.array(n_lst)

print(numpy.concatenate((m_array, n_array), axis=0))