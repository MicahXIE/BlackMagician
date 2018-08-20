'''
Input Format

The first line contains the integer N. 
The next N lines contains the N space separated elements of array A.

Output Format

Print the determinant of A.

Sample Input

2
1.1 1.1
1.1 1.1
Sample Output

0.0
'''

import numpy

num = int(input().strip())
lst = []

numpy.set_printoptions(legacy='1.13')

for _ in range(num):
    lst.append(list(map(float, input().strip().split())))
    
print(numpy.linalg.det(numpy.array(lst)))

