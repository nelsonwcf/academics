
public class MergeSort {
	static int[] sort(int[] a, int p, int q) {
		if (p == q) {
			int[] n = new int[1];
			n[0] = a[p];
			return n;
		} else {
			return mergesort(sort(a, p, (p + q) / 2), sort(a, (p + q) / 2 + 1, q));
		}
	}

	static int[] mergesort(int[] a, int[] b) {
		int[] x = new int[a.length + b.length];
		int ap = 0, bp = 0, xp = 0;

		while (xp < x.length) {
			if (ap < a.length && bp < b.length) {
				x[xp++] = a[ap] < b[bp] ? a[ap++] : b[bp++];
			} else if (ap < a.length) {
				x[xp++] = a[ap++];
			} else if (bp < b.length) {
				x[xp++] = b[bp++];
			}
		}

		return x;
	}

	public static void main(String args[]) {
		int[] a = { 7, 2, 13, 9, 26, 22, 1, 4, 3, 5, 11, 8, 2 }; // {1,2,3,4,5,7,8,9,11,13,22,26}
		int[] c;

		c = sort(a, 0, a.length - 1);

		for (int i = 0; i < c.length; i++)
			System.out.print(c[i] + " ");
	}

}
