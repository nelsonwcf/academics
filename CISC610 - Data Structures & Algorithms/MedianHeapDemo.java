import java.util.Arrays;
import java.util.Scanner;

//Enum the possible heap types (max-heap or min-heap).
enum HeapType {
	MAX, MIN
}

// Core of the code
// MedianHeap is a heap that put lower half smaller elements into a max-heap and
// upper half of bigger elements into a min-heap
// In this structure, the median is either the root of the heap (max or min)
// which has one more element than the other
// or the average of the root of both heaps, in the case they have the same
// number of elements
class MedianHeap {
	Heap maxHeap;
	Heap minHeap;
	double median; // median is of type double because sometimes the median is
					// the average of two integer which could have decimals.

	MedianHeap(int[] array) { // Constructor which builds both max and min heaps
								// from the array

		Arrays.sort(array);
		maxHeap = new Heap(HeapType.MAX);
		for (int i = 0; i <= (array.length - 1) / 2; i++) {
			maxHeap.push(array[i]);
		}

		minHeap = new Heap(HeapType.MIN);
		for (int i = ((array.length - 1) / 2) + 1; i < array.length; i++)
			minHeap.push(array[i]);

		medianUpdate();
	}

	double push(int n) { // Method to add a new element to the MedianHeap
		if (n < median) {
			maxHeap.push(n);
			rebalance();
		} else {
			minHeap.push(n);
			rebalance();
		}

		return median;
	}

	private void rebalance() { // When one of the heaps has more than one
								// element than the other
		while (maxHeap.size > minHeap.size + 1) { // this function is used to
													// rebalance both heaps by
													// moving the root
			minHeap.push(maxHeap.popRoot()); // of the heap with more elements
												// to the one with less elements
		}

		while (minHeap.size > maxHeap.size + 1) {
			maxHeap.push(minHeap.popRoot());
		}

		medianUpdate();
	}

	private void medianUpdate() { // Everytime a new element is added to the
									// structure, median has to be updated
		if (maxHeap.size == minHeap.size) {
			median = (double) (maxHeap.getRoot() + minHeap.getRoot()) / 2;
		} else if (maxHeap.size == minHeap.size + 1) {
			median = (maxHeap.getRoot());
		} else if (minHeap.size == maxHeap.size + 1) {
			median = (minHeap.getRoot());
		} else {
			System.out.println("Illegal State");
		}
		return;

	}

}

// This is the basic class that implements the Heap Structure. Depending on the
// type, it creates either a max-heap or a min-heap
// This class is used by the MedianHeap to create the two heaps (max and min)
// which is part of its structure
class Heap {
	int size;
	int[] array;
	HeapType type;

	Heap(int[] array, HeapType type) { // Constructor with array and type
		size = array.length - 1;
		this.array = array;
		this.type = type;

		if (type == HeapType.MAX)
			buildMaxHeap(array);
		else if (type == HeapType.MIN)
			buildMinHeap(array);
	}

	Heap(HeapType type) { // Constructor with empty array and type
		size = 0;
		this.array = new int[1];
		array[0] = 0;
		this.type = type;
	}

	int getRoot() { // Return the value of the root
		return array[1];
	}

	void printHeap() { // Print the content of the Heap
		for (int i = 1; i <= size; i++) {
			System.out.print(array[i] + " ");
		}
		System.out.println();
	}

	// Print the entire array which holds the heap
	void printHeapArray() {
		for (int i = 0; i < array.length; i++) {
			System.out.print(array[i] + " ");
		}
		System.out.println();
	}

	void push(int n) { // Insert a new element in the Heap
		if (size == array.length - 1) {
			array = Arrays.copyOf(array, (size + 1) * 2);
		}

		size++;
		array[size] = n;

		int parent = size / 2;
		int child = size;

		if (type == HeapType.MAX) {
			while (parent > 0 && array[parent] < array[child]) {
				int tmp = array[child];
				array[child] = array[parent];
				array[parent] = tmp;
				child = parent;
				parent = child / 2;
			}
		} else if (type == HeapType.MIN) {
			while (parent > 0 && array[parent] >= array[child]) {
				int tmp = array[child];
				array[child] = array[parent];
				array[parent] = tmp;
				child = parent;
				parent = child / 2;
			}

		}

	}

	int popRoot() { // Remove the root of the heap, returning it's value
		int tmp = array[size];
		array[size] = array[1];
		array[1] = tmp;

		size--;

		if (type == HeapType.MAX)
			maxHeapify(array, 1);
		else
			minHeapify(array, 1);

		return array[size + 1];
	}

	// Below are the heap private Heap methods
	private void buildMaxHeap(int[] array) { // Procedure to build the MaxHeap
		for (int i = size / 2; i >= 1; i--)
			maxHeapify(array, i);
	}

	private void maxHeapify(int[] array, int i) { // MaxHeapify procedure, used
													// by buildMaxHeap
		int left = 2 * i;
		int right = 2 * i + 1;
		int largest = 0;
		int tmp = 0;

		if (left <= size && array[left] > array[i])
			largest = left;
		else
			largest = i;

		if (right <= size && array[right] > array[largest])
			largest = right;

		if (largest != i) {
			tmp = array[i];
			array[i] = array[largest];
			array[largest] = tmp;
			maxHeapify(array, largest);
		}
		return;
	}

	private void buildMinHeap(int[] array) { // Procedure to build the MinHeap
		for (int i = size / 2; i >= 1; i--)
			minHeapify(array, i);
	}

	private void minHeapify(int[] array, int i) { // MinHeapify procedure, used
													// by buildMinHeap
		int left = 2 * i;
		int right = 2 * i + 1;
		int smallest = 0;
		int tmp = 0;

		if (left <= size && array[left] < array[i])
			smallest = left;
		else
			smallest = i;

		if (right <= size && array[right] < array[smallest])
			smallest = right;

		if (smallest != i) {
			tmp = array[i];
			array[i] = array[smallest];
			array[smallest] = tmp;
			minHeapify(array, smallest);
		}
		return;
	}

}

// Main code. Insert the initial array in the initialArray array.
public class MedianHeapDemo {
	public static void main(String args[]) {
		int[] initialArray = { 4, 3, 2, 90, 16, 78 }; // Insert the initial
														// Array
		MedianHeap mh = new MedianHeap(initialArray); // Create the MedianHeap -
														// see above

		System.out.println("Inital median: " + mh.median); // Show the initial
															// median from the
															// array "mh"
		System.out
				.println("Input any number of digits separated by space and press enter. To end, type any non-integer");

		try (Scanner sc = new Scanner(System.in)) { // Read integer and print
													// updated median after each
													// new integer

			while (sc.hasNext()) {
				if (sc.hasNextInt()) {
					System.out.println(mh.push(sc.nextInt()));
				} else {
					System.out.println("Non-Integer detected. Exiting...");
					return;
				}
			}
		}
	}
}
