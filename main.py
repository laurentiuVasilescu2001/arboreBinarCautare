class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Definim clasa pentru arborele binar
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def print_tree(self):
        self._print_tree_recursive(self.root, 0)

    def _print_tree_recursive(self, root, level):
        if root is not None:
            self._print_tree_recursive(root.right, level + 1)
            print("    " * level + str(root.key))
            self._print_tree_recursive(root.left, level + 1)

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insert_recursive(root.left, key)
        elif key > root.key:
            root.right = self._insert_recursive(root.right, key)
        return root

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self._delete_recursive(root.left, key)
        elif key > root.key:
            root.right = self._delete_recursive(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            min_node = self._find_min(root.right)
            root.key = min_node.key
            root.right = self._delete_recursive(root.right, min_node.key)
        return root

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search_recursive(root.left, key)
        return self._search_recursive(root.right, key)

    def get_max(self):
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current.key

    def get_min(self):
        if self.root is None:
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        return current.key

    def print_in_order(self):
        self._print_in_order_recursive(self.root)

    def _print_in_order_recursive(self, root):
        if root is not None:
            self._print_in_order_recursive(root.left)
            print(root.key, end=" ")
            self._print_in_order_recursive(root.right)

# Exemplu de utilizare
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

print("Arborele binar:")
print(bst.print_tree())
print("---------------")
print("Arborele prin in order")
print(bst.print_in_order())
print("---------------")
print("Search by key")
print(bst.search(30))
print("---------------")
print("Get min")
print(bst.get_min())
print("---------------")
print("Get max")
print(bst.get_max())
print("---------------")
print("Stergere")
bst.delete(30)
print(bst.print_tree())

