'''
Sample Input

1 2 3 4 5 6 7 8 9
Sample Output

[[1 2 3]
 [4 5 6]
 [7 8 9]]
 '''

import numpy

lst = list(map(int, input().strip().split()))
array = numpy.array(lst)
#wont change array by using reshape
#print(numpy.reshape(array,(3,3)))
array.shape = (3,3)
print(array)