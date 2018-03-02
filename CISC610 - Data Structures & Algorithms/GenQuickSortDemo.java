
public class GenQuickSortDemo {
	static <T extends Comparable<T>> void quicksort(T[] array) {
		if (array.length > 1)
			qsort(array, 0, array.length - 1);
	}

	static <T extends Comparable<T>> void qsort(T[] array, int left, int right) {

		if (left < right) {
			int l = left; // l will be incremented
			int r = right; // r will be decremented
			int p = (left + right) / 2; // pivot is just the middle element

			while (l <= r) {
				while (array[l].compareTo(array[p]) < 0)
					l++;
				while (array[r].compareTo(array[p]) > 0)
					r--;
				if (l <= r) {

					// The following block sets p to the current position of the
					// pivot value
					if (l == p)
						p = r;
					else if (r == p)
						p = l;

					// Quicksort Partitioning
					T tmp = array[l];
					array[l] = array[r];
					array[r] = tmp;
					l++;
					r--;
				}

			}
			qsort(array, left, p - 1);
			qsort(array, p + 1, right);
		}
	}

	public static void main(String args[]) {
		String[] array = {"Xereca", "Nelson", "Fernando", "Ana", "Jussara"}; // {1,2,3,4,5,7,8,9,11,13,22,26}

		quicksort(array);

		for (int i = 0; i < array.length; i++)
			System.out.print(array[i] + " ");
	}

}
