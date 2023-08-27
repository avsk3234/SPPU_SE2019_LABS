class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def add(self, key, value):
        self.root = self._add(self.root, key, value)

    def _add(self, node, key, value):
        if node is None:
            return Node(key, value)

        if key < node.key:
            node.left = self._add(node.left, key, value)
        else:
            node.right = self._add(node.right, key, value)

        node.height = 1 + max(self._height(node.left), self._height(node.right))

        balance = self._get_balance(node)

        if balance > 1 and key < node.left.key:
            return self._rotate_right(node)

        if balance < -1 and key > node.right.key:
            return self._rotate_left(node)

        if balance > 1 and key > node.left.key:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if balance < -1 and key < node.right.key:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            temp = self._get_min_node(node.right)
            node.key = temp.key
            node.value = temp.value
            node.right = self._delete(node.right, temp.key)

        if node is None:
            return node

        node.height = 1 + max(self._height(node.left), self._height(node.right))

        balance = self._get_balance(node)

        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._rotate_right(node)

        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._rotate_left(node)

        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def get(self, key):
        node = self.root
        while node is not None:
            if key == node.key:
                return node.value
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return None

    def _height(self, node):
        if node is None:
            return 0
        return node.height
       
    def _get_balance(self, root):
        if not root:
            return 0
        return self._height(root.left) - self._height(root.right)

    def _rotate_left(self, node):
        right_node = node.right
        right_left_node = right_node.left

        right_node.left = node
        node.right = right_left_node

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        right_node.height = 1 + max(self._height(right_node.left), self._height(right_node.right))

        return right_node

    def _rotate_right(self, node):
        left_node = node.left
        left_right_node = left_node.right

        left_node.right = node
        node.left = left_right_node

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        left_node.height = 1 + max(self._height(left_node.left), self._height(left_node.right))

        return left_node

    def traverse(self, node=None):
        if node is None:
            node = self.root

        if node.left:
            yield from self.traverse(node.left)

        yield node.key

        if node.right:
            yield from self.traverse(node.right)

# create an empty AVL tree
tree = AVLTree()

# add some keywords and their meanings
tree.add("apple", "a fruit")
tree.add("banana", "a fruit")
tree.add("carrot", "a vegetable")

# display the whole data sorted in ascending order
print("Ascending order:")
for key in sorted(tree.traverse()):
    print(key, tree.get(key))

# display the whole data sorted in descending order
print("Descending order:")
for key in sorted(tree.traverse(), reverse=True):
    print(key, tree.get(key))

# update the value of an entry
tree.add("apple", "a type of computer")

# display the updated value
print("Updated value of 'apple':", tree.get("apple"))

# delete a keyword
tree.delete("carrot")

# display the whole data sorted in ascending order
print("Ascending order:")
for key in sorted(tree.traverse()):
    print(key, tree.get(key))

# find how many maximum comparisons may require for finding a keyword
max_comparisons = tree._height(tree.root)
print("Maximum comparisons for finding a keyword:", max_comparisons)

