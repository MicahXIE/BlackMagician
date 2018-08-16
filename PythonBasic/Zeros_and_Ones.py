'''
Input Format

A single line containing the space-separated integers.

Constraints

1 <= each integer <= 3

Output Format

First, print the array using the numpy.zeros tool and then print the array with the numpy.ones tool.

Sample Input 0

3 3 3
Sample Output 0

[[[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]]
[[[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]]
Explanation 0

Print the array built using numpy.zeros and numpy.ones tools and you get the result as shown.
'''


import numpy

# tuple is better because the input integer numbers is random
tp = tuple(map(int,input().strip().split()))

print(numpy.zeros(tp, dtype = numpy.int))
print(numpy.ones(tp, dtype = numpy.int))