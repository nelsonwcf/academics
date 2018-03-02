
public class BubbleSortDemo {
	static void bubblesort(int[] a) {
		boolean repeat = true;

		while (repeat == true) {
			repeat = false;
			for (int i = 0; i < a.length - 1; i++) {
				if (a[i + 1] < a[i]) {
					int tmp = a[i];
					a[i] = a[i + 1];
					a[i + 1] = tmp;
					repeat = true;
				}
			}
		}

	}

	public static void main(String args[]) {
		int[] a = { 7, 2, 13, 9, 26, 22, 1, 4, 3, 5, 11, 8, 2 }; // {1,2,3,4,5,7,8,9,11,13,22,26}

		bubblesort(a);

		for (int i = 0; i < a.length; i++)
			System.out.print(a[i] + " ");
	}
}
