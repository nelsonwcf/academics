import java.util.*;

public class Fibo {

	public static void main(String args[]) {
		HashMap<Integer, Integer> hm = new HashMap<>();
//		System.out.println(fibonacci_tr(12, 0,1));
		System.out.println(fibonacci(12, hm));

	}

	// Dynamic programming in recursion
	static int fibonacci(int n, HashMap<Integer, Integer> hm) {
		int res;
		if (hm.containsKey(n))
			return hm.get(n);

		if (n <= 2)
			return 1;
		else
			res = fibonacci(n - 1, hm) + fibonacci(n - 2, hm);
		hm.put(n, res);
		return res;
	}

	// my solution - tail recursion
//	static int fibonacci_tr(int n, int f_1, int f_2) {
//		if (n <= 0)
//			return -1; // Undefined
//		else if (n <= 1)
//			return f_2;
//		else
//			return fibonacci_tr(n - 1, f_2, f_1 + f_2);
//	}
}