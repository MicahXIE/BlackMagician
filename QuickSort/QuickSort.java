/* 
Quick Sort Summary
Quicksort can operate in-place on an array, requiring small additional amounts of memory
to perform the sorting. It is very similar to selection sort, except that it does not always 
choose worst-case partition.Mathematical analysis of quicksort shows that, on average, 
the algorithm takes O(n log n) comparisons to sort n items. In the worst case, 
it makes O(n2) comparisons, though this behavior is rare.
*/
import java.util.Arrays;

class QuickSort{
	public static void main(String[] args){
		QuickSort qs = new QuickSort();
		int a[] = {5,4,3,2,1};
		System.out.println(Arrays.toString(a));
		qs.quicksort(a, 0, a.length-1);
		System.out.println(Arrays.toString(a));		
	}

	public void quicksort(int [] array, int low, int high){
		if (array.length <= 1){
			return;
		}

		if(low > high){
			return;
		}

		int key = array[low];
		int i=low, j=high;

		while(i < j){

			while(i<j && array[j] > key){
				j--;
			}

			while(i<j && array[i] <= key){
				i++;
			}

			if (i < j){
				swap(array,i,j);
			}
		}
		swap(array,low,i);

		quicksort(array,low,i-1);
		quicksort(array,i+1,high);

	}

	public void swap(int[] array, int i, int j){
		int p = array[i];
		array[i] = array[j];
		array[j] = p;

		// notice: can't use below method since i can equal j
		//array[i] = array[i] + array[j];
		//array[j] = array[i] - array[j];
		//array[i] = array[i] - array[j];
	}
}