class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)

        # If the tree is empty, set the root to the new node
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            parent = None

            while True:
                parent = current

                # Go to the left subtree if data is less than current node's data
                if data < current.data:
                    current = current.left

                    # If left child is None, insert the new node here
                    if current is None:
                        parent.left = new_node
                        return
                else:
                    # Go to the right subtree if data is greater or equal
                    current = current.right

                    # If right child is None, insert the new node here
                    if current is None:
                        parent.right = new_node
                        return

    def search(self, data):
        current = self.root
        print("Visiting elements:", end=" ")

        # Traverse the tree until finding the data or reaching a leaf
        while current is not None and current.data != data:
            print(current.data, end=" ")

            # Go to the left subtree if data is smaller than the current node's data
            if data < current.data:
                current = current.left
            # Otherwise, go to the right subtree
            else:
                current = current.right

        # If current is None, data was not found
        if current is None:
            return None

        # Return the node containing the data
        return current

    def pre_order_traversal(self, node):
        if node is not None:
            print(node.data, end=" ")
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)

    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.data, end=" ")
            self.inorder_traversal(node.right)

    def post_order_traversal(self, node):
        if node is not None:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.data, end=" ")


# Main execution
if __name__ == "__main__":
    bst = BinarySearchTree()
    array = [27, 14, 35, 10, 19, 31, 42]

    for value in array:
        bst.insert(value)

    # Searching for elements
    element_to_search = 31
    result = bst.search(element_to_search)
    if result is not None:
        print(f"\n[{result.data}] Element found.")
    else:
        print(f"\n[ x ] Element not found ({element_to_search}).")

    element_to_search = 15
    result = bst.search(element_to_search)
    if result is not None:
        print(f"\n[{result.data}] Element found.")
    else:
        print(f"\n[ x ] Element not found ({element_to_search}).")

    # Traversals
    print("\nPreorder traversal: ", end="")
    bst.pre_order_traversal(bst.root)

    print("\nInorder traversal: ", end="")
    bst.inorder_traversal(bst.root)

    print("\nPost order traversal: ", end="")
    bst.post_order_traversal(bst.root)