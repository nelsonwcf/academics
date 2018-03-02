import java.io.*;
import java.util.*;

public class MinCutDemo {
	public static void main(String args[]) {
		// Generate the graph
		// Using statically allocated matrix of the size 200 + 1.
		int[][] graph = new int[6][6];
		for (int i = 0; i < graph.length; i++)
			for (int j = 0; j < graph.length; j++) {
				graph[i][j] = 0;
			}

		// Loading the input file into the graph structure
		// Position [0] will be used to mark vertices that have been merged
		try (Scanner s = new Scanner(new FileInputStream("input\\mincut2.txt"))) {
			int i = 0, j = 0;

			while (s.hasNextLine()) {
				try (Scanner sl = new Scanner(s.nextLine())) {
					i = sl.nextInt();

					graph[i][0] = i;
					graph[0][i] = i;
					while (sl.hasNextInt()) {
						j = sl.nextInt();
						graph[i][j] = 1;
						graph[j][i] = 1;
					}
				}
			}
		} catch (FileNotFoundException e) {
			System.out.println("File Not Found.");
		}

		Random rand = new Random();
		int r1 = rand.nextInt(graph.length - 1) + 1;
		int r2 = rand.nextInt(graph.length - 1) + 1;
		r1 = 5;
		r2 = 1;
		System.out.println(r1 + " " + r2);
		
		

		if (graph[r1][r2] == 1)
			graph = mergeV(graph, r1, r2);
		
		pgraph(graph);

	}

	// Merge to vertices
	static int[][] mergeV(int[][] g, int vi, int vf) {
		int[][] g1 = new int[g.length][g.length];

		for (int i = 0; i < g.length; i++)
			for (int j = 0; j < g.length; j++)
				g1[i][j] = g[i][j];

		for (int i = 1; i < g.length; i++) {
			g1[vf][i] = g1[vf][i] + g[vi][i];
			g1[i][vf] = g1[i][vf] + g[i][vi];
		}

		g1[vf][vf] = 0;

		g1 = remV(g1, vi);

		return g1;
	}

	// Function used to remove
	static int[][] remV(int[][] g, int v) {
		if (g.length == 0)
			return null;

		int[][] g1 = new int[g.length - 1][g.length - 1];
		int index = 0;

		// Getting the row and column
		for (int i = 0; i < g.length; i++)
			if (g[0][i] == v) {
				index = i;
				break;
			}

		// Remove specified line and column from the matrix
		int i1 = 0, j1 = 0;
		for (int i = 0; i < g.length; i++) {
			j1 = 0;
			for (int j = 0; j < g.length; j++) {
				if (j != index) {
					g1[i1][j1] = g[i][j];
					j1++;
				}
			}
			if (i != index) {
				i1++;
			}
		}
		return g1;
	}

	static void pgraph(int[][] g) {
		for (int k = 0; k < g.length; k++) {
			for (int l = 0; l < g.length; l++) {
				System.out.print(g[k][l] + " ");
			}
			System.out.println();
		}
		System.out.println();
	}
}
