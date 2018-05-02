"""
Quick Sort Summary
Quicksort can operate in-place on an array, requiring small additional amounts of memory
to perform the sorting. It is very similar to selection sort, except that it does not always 
choose worst-case partition.Mathematical analysis of quicksort shows that, on average, 
the algorithm takes O(n log n) comparisons to sort n items. In the worst case, 
it makes O(n2) comparisons, though this behavior is rare.
"""
def swap(array, index1, index2):
	p = array[index1]
	array[index1] = array[index2]
	array[index2] = p


def quicksort(array, low, high):

	if (low > high):
		return

	key = array[low]
	i = low
	j = high

	while(i < j):

		while(i < j and array[j] > key):
			j-=1

		while(i < j and array[i] <= key):
			i+=1

		if(i < j):
			swap(array, i, j)

	swap(array, low, i)
	quicksort(array, low, i-1)
	quicksort(array, i+1, high)

if __name__ == '__main__':
	array = [5, 4, 3, 2, 1]
	print("before sorting, the list is :", array)
	quicksort(array, 0, len(array)-1)
	print("after sorting, the list is :", array)
