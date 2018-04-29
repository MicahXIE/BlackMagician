/*
Binary search compares the target value to the middle element of the array; if they are unequal, 
the half in which the target cannot lie is eliminated and the search continues on the remaining half 
until it is successful. If the search ends with the remaining half being empty, 
the target is not in the array.
*/
class BinarySearch{

	public static void main(String[] args){
		int sortedArray[] = {1, 3, 5, 7, 9};
		int key = 6;
		int low = 0, high = sortedArray.length-1;
		BinarySearch bs = new BinarySearch();
		int index = bs.BinarySearch(sortedArray, key, low, high);
		System.out.println("the index of the number is :" + index);

	}

	public int BinarySearch(int[] sortedArray, int key, int low, int high){

		while(low < high){
			int mid = (low + high)/2;
			if (sortedArray[mid] < key){
				low = mid + 1;
				BinarySearch(sortedArray, key, low, high);
			} else if (sortedArray[mid] > key) {
				high = mid -1;
				BinarySearch(sortedArray, key, low, high);
			} else {
				return mid;
			}
		}

		return -1;

	}
}
