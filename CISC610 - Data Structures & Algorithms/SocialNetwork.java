import java.util.*;

// Defining Vertex object, used in the BFS algorithm later
class Vertex {
	int id;
	String name;
	VColor color;
	Vertex predecessor;
	int distance;

	Vertex(String s, int id) {
		this.id = id;
		name = s;
		color = VColor.white;
		predecessor = null;
		distance = -1;
	}
}

enum VColor {
	white, gray, black;
}

public class SocialNetwork {
	int maxNetworkSize;
	int networkSize;

	String[] path;
	int currentPos;

	// This is the graph structure - statically allocated matrix representing
	// the graph. In a distributed environment like Facebook or LinkedIn, this
	// structure would never be a good solution due to the distributed
	// environment; dynamically allocated would be preferred. For this
	// assignment, this should be enough.
	int[][] connections;

	// This map will convert ID number to Name. Can be extended to more complex
	// objects instead of just the name.
	HashMap<String, Integer> map;
	HashMap<Integer, String> reverseMap;

	// Constructor - receives the maximum number of network members, statically
	// allocated.
	public SocialNetwork(int maxNetworkSize) {
		this.maxNetworkSize = maxNetworkSize;
		connections = new int[maxNetworkSize][maxNetworkSize];
		map = new HashMap<>();
		reverseMap = new HashMap<>();
		networkSize = 0;
		path = new String[maxNetworkSize];
	}

	// This method inserts a new member in the network. If the network is full
	// or the name already exists, it returns false. If the new members is
	// successfully added, it returns true. For this exercise, members are
	// defined by name.
	boolean insert(String name) {
		if (map.containsKey(name) || networkSize == maxNetworkSize)
			return false;

		connections[networkSize][networkSize] = 1;
		map.put(name, networkSize);
		reverseMap.put(networkSize, name);
		networkSize++;
		return true;
	}

	// Returns true if people are successfully connected or are already
	// connected. Returns false if someone doesn't exist or if the network is
	// empty.
	boolean connect(String name1, String name2) {
		if (!map.containsKey(name1) || !map.containsKey(name2) || networkSize == 0)
			return false;

		connections[map.get(name1)][map.get(name2)] = 1;
		connections[map.get(name2)][map.get(name1)] = 1;
		return true;
	}

	// This function displays the entire social network.
	void showAll() {
		for (String s : map.keySet()) {
			System.out.println(s);
			System.out.print("\t");
			for (int i = 0; i < networkSize; i++)
				if (map.get(s) != i && connections[map.get(s)][i] == 1)
					System.out.print(reverseMap.get(i) + " ");
			System.out.println();
			System.out.println("--------");
		}
	}

	// Uses the BFS algorithm to shows all nodes at specific distance from
	// the vertex 'name'. 'distance' variable selects how many hops from name.
	void showDistance(String name, int distance) {

		int id = map.get(name);

		HashMap<Integer, Vertex> vertMap = new HashMap<>();
		map.forEach((s, p) -> vertMap.put(p, new Vertex(s, p)));
		vertMap.get(id).color = VColor.gray;
		vertMap.get(id).predecessor = null;
		vertMap.get(id).distance = 0;

		LinkedList<Vertex> q = new LinkedList<>();
		q.add(vertMap.get(id));

		while (!q.isEmpty()) {
			Vertex u = q.removeFirst();
			for (int i = 0; i < maxNetworkSize; i++) {
				if (connections[u.id][i] == 1) {
					Vertex v = vertMap.get(i);
					if (v.color == VColor.white) {
						v.color = VColor.gray;
						v.distance = u.distance + 1;
						v.predecessor = u;
						q.add(v);
					}
				}
			}
			u.color = VColor.black;
		}
		System.out.print(distance + ": ");
		vertMap.forEach((s, p) -> {
			if (p.distance == distance)
				System.out.print(p.name + " ");
		});
	}

	// Using BFS, this function shows a path between two vertices.
	void showPath(String origin, String goal) {
		int id = map.get(origin);
		int id2 = map.get(goal);

		HashMap<Integer, Vertex> vertMap = new HashMap<>();
		map.forEach((s, p) -> vertMap.put(p, new Vertex(s, p)));
		vertMap.get(id).color = VColor.gray;
		vertMap.get(id).predecessor = null;
		vertMap.get(id).distance = 0;

		LinkedList<Vertex> q = new LinkedList<>();
		q.add(vertMap.get(id));

		while (!q.isEmpty()) {
			Vertex u = q.removeFirst();
			for (int i = 0; i < maxNetworkSize; i++) {
				if (connections[u.id][i] == 1) {
					Vertex v = vertMap.get(i);
					if (v.color == VColor.white) {
						v.color = VColor.gray;
						v.distance = u.distance + 1;
						v.predecessor = u;
						q.add(v);
					}
				}
			}
			u.color = VColor.black;
		}

		Vertex u = vertMap.get(id2);
		recBackTrackPrint(vertMap.get(id).name, u);
		System.out.println();
	}
	
	// Small function to print the path in the reverse order of leaf to root 
	void recBackTrackPrint(String origin, Vertex u) {
		if (!u.name.equals(origin))
			if (u.predecessor != null)
				recBackTrackPrint(origin, u.predecessor);
			else {
				System.out.println("Path not found");
				return;
			}
		System.out.print(u.name + " ");
	}

	public static void main(String args[]) {
		SocialNetwork sn = new SocialNetwork(100); // <- This defines the
													// maximum number of
													// vertices (people) for
													// this network
		/*
		 * sn.insert("Nelson"); sn.insert("Ana"); sn.insert("John");
		 * sn.insert("Bruna"); sn.insert("Dani"); sn.connect("Nelson", "Ana");
		 * sn.connect("Ana", "John"); sn.connect("John", "Bruna");
		 * sn.showPath("Nelson", "Bruna");
		 */

		sn.insert("Nelson");
		sn.insert("Dani");
		sn.insert("Diana");
		sn.insert("Diana");

		sn.connect("Nelson", "Diana");
		sn.connect("Nelson", "Dani");
		sn.showPath("Nelson", "Diana");
		sn.showDistance("Nelson", 1);
		
		sn.showAll();

		/*
		 * sn.insert("Marcos"); sn.insert("Bruna"); sn.insert("Lina");
		 * sn.insert("Miller"); sn.insert("Stephen");
		 * 
		 * sn.connect("Nelson", "Dani"); sn.connect("Nelson", "Diana");
		 * sn.connect("Nelson", "Marcos"); sn.connect("Nelson", "Bruna");
		 * sn.connect("Nelson", "Lina"); sn.connect("Nelson", "Stephen");
		 * 
		 * sn.connect("Dani", "Diana"); sn.connect("Dani", "Marcos");
		 * sn.connect("Dani", "Bruna");
		 * 
		 * sn.connect("Diana", "Bruna"); sn.connect("Diana", "Marcos");
		 * 
		 * sn.connect("Marcos", "Lina"); sn.connect("Lina", "Stephen");
		 * sn.connect("Stephen", "Miller");
		 * 
		 * // sn.showDistance("Nelson", 2); sn.showPath("Marcos", "Miller");
		 * 
		 * sn.showAll();
		 * 
		 */
	}
}
