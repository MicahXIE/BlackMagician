'''
Input Format

The first line contains the space separated value of the coefficients in P. 
The second line contains the value of x.

Output Format

Print the desired value.

Sample Input

1.1 2 3
0
Sample Output

3.0

'''

import numpy

P = list(map(float, input().strip().split()))
x = float(input().strip())

print(numpy.polyval(P, x))