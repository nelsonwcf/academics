// Debugging Exceptions
@SuppressWarnings("serial")
class NoLeftChildException extends RuntimeException {
}

@SuppressWarnings("serial")
class NoRightChildException extends RuntimeException {
}

@SuppressWarnings("serial")
class NoGrandParentException extends RuntimeException {
}

@SuppressWarnings("serial")
class ShouldNotBeHereException extends RuntimeException {
}

class RBNode<T extends Comparable<T>> {
	T value;
	boolean black;
	RBNode<T> left;
	RBNode<T> right;
	RBNode<T> parent;

	RBNode() {
		black = true;
		left = null;
		right = null;
		parent = null;
	}

	RBNode(T val) {
		this();
		value = val;
	}

	RBNode(T val, RBNode<T> parent) {
		this(val);
		this.parent = parent;
	}

	RBNode(T val, RBNode<T> parent, boolean black) {
		this(val, parent);
		this.black = black;
	}
}

public class RBTree<T extends Comparable<T>> {
	public final int DIRECTION_LEFT = 0;
	public final int DIRECTION_RIGHT = 1;

	RBNode<T> root;
	int size;

	public RBTree() {
		root = null;
		size = 0;
	}

	public RBNode<T> insert(T value) {
		if (root == null) {
			root = new RBNode<>(value, root, true);
			return root;
		} else {
			RBNode<T> tmp = root;
			boolean found = false;
			while (found == false) {
				if (value.compareTo(tmp.value) <= 0) {
					if (tmp.left == null) {
						found = true;
						try {
							tmp.left = new RBNode<>(value, tmp, false);
							tmp = tmp.left;
						} catch (OutOfMemoryError e) {
							System.out.println("Out of memory");
							System.exit(-1);
						}
					} else
						tmp = tmp.left;
				} else {
					if (tmp.right == null) {
						found = true;
						try {
							tmp.right = new RBNode<>(value, tmp, false);
							tmp = tmp.right;
						} catch (OutOfMemoryError e) {
							System.out.println("Out of memory");
							System.exit(-1);
						}
					} else
						tmp = tmp.right;
				}
			}
			// Restoring RBTree properties
			RBFixUp(tmp);
			return tmp;
		}
	}

	// Workaround for avoiding addressing unallocated node's pointers
	private void setParent(RBNode<T> node, RBNode<T> parent) {
		if (node != null)
			node.parent = parent;
		return;
	}

	void rotateNode(RBNode<T> node, int direction) {
		if (node == null)
			return;

		// is the node root?
		boolean isRoot = node == root ? true : false;
		// is the node left child?
		boolean isLeft = (isRoot == false && node.parent.left == node) ? true : false;

		RBNode<T> parent, child;
		parent = isRoot == false ? node.parent : root;

		if (direction == DIRECTION_RIGHT) {
			if (node.left == null)
				throw (new NoLeftChildException());
			child = node.left;

			// Fix right child's child pointers
			setParent(child.right, node);

			// Fix node pointers
			setParent(node, child);
			node.left = child.right;

			// Fix child's children pointers
			child.right = node;

			// Fix child's parent pointer
			if (isRoot) {
				root = child;
				setParent(child, null);
			} else if (isLeft) {
				parent.left = child;
				setParent(child, parent);
			} else {
				parent.right = child;
				setParent(child, parent);
			}
		}

		else if (direction == DIRECTION_LEFT) {
			if (node.right == null)
				throw (new NoRightChildException());
			child = node.right;

			// Fix left child's child pointers
			setParent(child.left, node);

			// Fix node pointers
			setParent(node, child);
			node.right = child.left;

			// Fix child's children pointers
			child.left = node;

			// Fix child parent pointer
			if (isRoot) {
				root = child;
				setParent(child, null);
			} else if (isLeft) {
				parent.left = child;
				setParent(child, parent);
			} else {
				parent.right = child;
				setParent(child, parent);
			}
		}
	}

	void setGrandparentColorBlack(RBNode<T> node, boolean flag) {
		if (node.parent.parent == null)
			throw (new NoGrandParentException());
		else
			node.parent.parent.black = flag;
	}

	void setParentColorBlack(RBNode<T> node, boolean flag) {
		node.parent.black = flag;
	}

	boolean parentColorBlack(RBNode<T> node) {
		return node.parent.black;
	}

	void setUncleColorBlack(RBNode<T> node, boolean flag) {
		RBNode<T> grandparent = node.parent.parent;

		if (grandparent == null)
			throw (new NoGrandParentException());
		else {
			if (grandparent.left == node.parent) {
				if (grandparent.right != null)
					grandparent.right.black = flag;
			} else {
				if (grandparent.left != null)
					grandparent.left.black = flag;
			}
		}
	}

	boolean uncleColorBlack(RBNode<T> node) {
		RBNode<T> grandparent = node.parent.parent;

		if (grandparent == null)
			throw (new NoGrandParentException());
		else {
			if (grandparent.left == node.parent)
				return grandparent.right != null ? grandparent.right.black : true;
			else
				return grandparent.left != null ? grandparent.left.black : true;
		}
	}

	void RBFixUp(RBNode<T> node) {
		// Case 0: node is root - color node black
		if (node == root)
			node.black = true;

		// Case 1: Parent is black - nothing to do
		else if (parentColorBlack(node))
			return;

		// Case 2: Parent and uncle are red
		else if (!uncleColorBlack(node)) {
			setParentColorBlack(node, true);
			setUncleColorBlack(node, true);
			setGrandparentColorBlack(node, false);
			RBFixUp(node.parent.parent);
		}

		// Case 3: left child of left parent with black uncle
		else if (node.parent.parent.left == node.parent && node.parent.left == node) {
			rotateNode(node.parent.parent, DIRECTION_RIGHT);
			node.black = false;
			node.parent.black = true;
			node.parent.right.black = false;
		}

		// Case 4: right child of left parent with black uncle
		else if (node.parent.parent.left == node.parent && node.parent.right == node) {
			rotateNode(node.parent, DIRECTION_LEFT);
			rotateNode(node.parent, DIRECTION_RIGHT);
			node.black = true;
			node.left.black = false;
			node.right.black = false;
		}

		// Case 5: right child of right parent with black uncle
		else if (node.parent.parent.right == node.parent && node.parent.right == node) {
			rotateNode(node.parent.parent, DIRECTION_LEFT);
			node.black = false;
			node.parent.black = true;
			node.parent.left.black = false;
		}

		// Case 6: left child of right parent with black uncle
		else if (node.parent.parent.right == node.parent && node.parent.left == node) {
			rotateNode(node.parent, DIRECTION_RIGHT);
			rotateNode(node.parent, DIRECTION_LEFT);
			node.black = true;
			node.left.black = false;
			node.right.black = false;
		}

		// Program should never reach this place
		else {
			throw (new ShouldNotBeHereException());
		}
	}

	RBNode<T> getNode(T value) {
		return auxGetNode(root, value);
	}

	private RBNode<T> auxGetNode(RBNode<T> node, T value) {
		if (node == null)
			return null;
		else {
			if (value.compareTo(node.value) == 0)
				return node;
			else if (value.compareTo(node.value) < 0)
				return auxGetNode(node.left, value);
			else
				return auxGetNode(node.right, value);
		}
	}

	boolean isLeftChild(RBNode<T> node) {
		if (node == null || node.parent == null)
			return false;
		else
			return node.parent.left == node ? true : false;
	}

	boolean isRoot(RBNode<T> node) {
		if (node == root)
			return true;
		else
			return false;
	}
	
	RBNode<T> inOrderSuccessor(RBNode<T> node) {
		return inOrderSuccessorAux(node.right);
	}
		
	RBNode<T> inOrderSuccessorAux(RBNode<T> node) {
		if (node == null)
			return null;
		else if (node.left == null)
			return node;
		else
			return inOrderSuccessorAux(node.left);
	}

	void exchangeValues(RBNode<T> node1, RBNode<T> node2) {
		RBNode<T> aux = new RBNode<>();
		
		// replace the contents of the tree here
		// so far, only color and value
		aux.black = node1.black;
		aux.value = node1.value;
		node1.black = node2.black;
		node1.value = node2.value;
		node2.black = aux.black;
		node2.value = aux.value;
	}

	RBNode<T> remove(RBNode<T> node) {
		if (node == null)
			return null;
		else {
			// Node is a leaf
			if (node.left == null && node.right == null) {
				if (isRoot(node))
					root = null;
				else if (isLeftChild(node))
					node.parent.left = null;
				else
					node.parent.right = null;
			}

			// Node has two children
			else if (node.left != null && node.right != null) {
				RBNode<T> aux;
				
				exchangeValues(node, aux = inOrderSuccessor(node));
				if (isLeftChild(aux))
					aux.parent.left = null;
				else
					aux.parent.right = null;
			}

			// Node has only left child
			else if (node.right == null) {
				exchangeValues(node, node.left);
				node.left = null;
			}

			// Node has only right child
			else {
				exchangeValues(node, node.right);
				node.right = null;
			}
		}
		return node;
	}
}