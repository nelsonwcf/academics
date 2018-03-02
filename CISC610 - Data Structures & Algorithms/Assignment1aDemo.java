
public class Assignment1aDemo {
	public static void main(String args[]) {
		pascalTriangle(10); // <- substitute the number between brackets for the depth of the Pascal Triangle					

	}

	// Requested function - Prints the PascalTriangle using depth variable
	static void pascalTriangle(int depth) {
		for (int i = 1; i <= depth; i++) {
			for (int j = 1; j <= i; j++) {
				System.out.print(pT(i, j) + " ");
			}
			System.out.println();
		}

	}
	
	// Recursive function that calculates the Pascal Triangle values using summation property
	static private int pT(int row, int column) {
		// Return -1 if the input is illegal
		if (column > row | row <= 0 | column <= 0)
			return -1;
		
		// Base case -> element is either the left or right edges -- returns 1 in this case
		if (column == 1 | column == row) 
			return 1;
		// Recursive case that invokes the function again until the base case is reached (sum of edges)
		else 
			return pT(row - 1, column) + pT(row - 1, column - 1);
	}

}
