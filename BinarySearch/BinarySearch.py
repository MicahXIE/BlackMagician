"""
Binary search compares the target value to the middle element of the array; if they are unequal, 
the half in which the target cannot lie is eliminated and the search continues on the remaining half 
until it is successful. If the search ends with the remaining half being empty, 
the target is not in the array.
"""
def BinarySearch(sortedArray, key, low, high):
	while low < high:
		mid = (low + high)//2
		if sortedArray[mid] < key:
			low = mid + 1
			BinarySearch(sortedArray, key, low, high)
		elif sortedArray[mid] > key:
			high = mid - 1
			BinarySearch(sortedArray, key, low, high)
		else:
			return mid

	return -1

if __name__ == "__main__":
	sortedArray = [1, 3, 5, 7, 9]
	key = 7
	low, high = 0, len(sortedArray)-1
	index = BinarySearch(sortedArray, key, low, high)
	print("the index of the number is %d" % index)