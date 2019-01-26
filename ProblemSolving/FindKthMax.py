"""
use quick sort to get the kth max value in the array

recursion return issue, very interesting:
https://www.jianshu.com/p/c1dcf423e128
"""

def swap(array, index1, index2):
	p = array[index1]
	array[index1] = array[index2]
	array[index2] = p


def quicksort(array, low, high, k):

	if (low > high):
		return

	key = array[low]
	i = low
	j = high

	while(i < j):

		while(i < j and array[j] < key):
			j-=1

		while(i < j and array[i] >= key):
			i+=1

		if(i < j):
			swap(array, i, j)

	swap(array, low, i)

	print(array)

	if i > k:
		return quicksort(array, low, i-1, k)
	elif i < k:
		return quicksort(array, i+1, high, k)
	else:
		return array[i]


if __name__ == '__main__':
	#array = [5, 4, 3, 2, 1]
	array = [1, 2, 3, 4, 5]
	# start with 0, so it is 4th max
	res = quicksort(array, 0, len(array)-1, 3)
	print("the 4th max value is ", res)
