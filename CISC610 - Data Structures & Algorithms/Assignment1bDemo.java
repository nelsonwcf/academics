import java.io.*;
import java.util.*;

public class Assignment1bDemo {
	static int inversions;

	public static void main(String args[]) {

		ArrayList<Integer> a = new ArrayList<>();

		// Load number into List structure for sorting
		File f0 = new File("input/IntegerArray.txt"); // Change this to the location of the file
		try (BufferedReader f = new BufferedReader(new FileReader(f0))) {
			String s;

			while ((s = f.readLine()) != null)
				a.add(Integer.parseInt(s));

		} catch (IOException e) {
			p("File not Found");
		}

		Integer[] list = new Integer[a.size()];
		a.toArray(list);

		mergeSort(list, 0, a.size() - 1);

		/* Uncomment this block to print the results of the sorting
		for (int i = 0; i < list.length; i++)
			System.out.println(list[i]);
		*/


		p("Total Inversions: " + inversions);

	}

	// MergeSort function
	public static <T extends Comparable<T>> void mergeSort(T[] array, int start, int end) {
		if (start < end) {
			int mid = (start + end) / 2;
			mergeSort(array, start, mid);
			mergeSort(array, mid + 1, end);
			merge(array, start, end);
		}
	}

	// Merge portion of the MergeSort modified to count inversions
	private static <T extends Comparable<T>> void merge(T[] array, int start, int end) {
		int mid = (start + end) / 2;
		int i = start;
		int j = mid + 1;
		int k = start;

		// Inefficient - Needs optimization but should work as a proof of
		// concept
		T[] temp = Arrays.copyOf(array, array.length);

		// leftSmallest and neverRun are the key variables for counting
		// inversions
		boolean leftSmallest = false;
		boolean neverRun = true;

		while (i <= mid && j <= end) {
			if (temp[i].compareTo(temp[j]) < 0) {
				array[k] = temp[i];
				i++;
			} else {
				array[k] = temp[j];
				j++;
				leftSmallest = true;
			}

			// MergeSort modification to count inversions below
			// If the element from the right sub-array is smaller than the the
			// one from the right
			// All elements not already added from the left array are counted
			// ONCE
			if (leftSmallest == true && neverRun == true) {
				inversions += mid - i + 1;
				neverRun = false;
			}

			k++;
		}

		while (i <= mid) {
			array[k] = temp[i];
			i++;
			k++;
		}

		while (j <= end) {
			array[k] = temp[j];
			j++;
			k++;
		}

	}

	// Auxiliary function
	static void p(Object o) {
		System.out.print(o + " ");
	}
}
