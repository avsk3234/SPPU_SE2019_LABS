class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class Dictionary:
    def __init__(self, size):
        self.size = size
        self.hash_table = [None] * size

    def _hash_function(self, key):
        """Hash function to map key to an index in the hash table."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert a (key, value) pair into the dictionary."""
        index = self._hash_function(key)
        if self.hash_table[index] is None:
            # If the index is empty, create a new node with the key and value
            self.hash_table[index] = Node(key, value)
        else:
            # If the index is not empty, handle collision using chaining
            current = self.hash_table[index]
            while current.next is not None:
                if current.key == key:
                    # If the key already exists, replace the value
                    current.value = value
                    return
                current = current.next
            if current.key == key:
                # If the key already exists at the last node, replace the value
                current.value = value
            else:
                # If the key does not exist, create a new node and append it
                current.next = Node(key, value)

    def find(self, key):
        """Find the value associated with a given key in the dictionary."""
        index = self._hash_function(key)
        current = self.hash_table[index]
        while current is not None:
            if current.key == key:
                # If the key is found, return the corresponding value
                return current.value
            current = current.next
        # If the key is not found, return None
        return None

    def delete(self, key):
        """Delete a key-value pair from the dictionary."""
        index = self._hash_function(key)
        current = self.hash_table[index]
        previous = None
        while current is not None:
            if current.key == key:
                # If the key is found, remove the corresponding node
                if previous is None:
                    # If the node is the first in the chain, update the head
                    self.hash_table[index] = current.next
                else:
                    # If the node is not the first, update the previous node's next pointer
                    previous.next = current.next
                return
            previous = current
            current = current.next

    def display(self):
        """Display the contents of the dictionary."""
        for index in range(self.size):
            current = self.hash_table[index]
            print(f'Index {index}:', end=' ')
            while current is not None:
                print(f'({current.key}, {current.value})', end=' -> ')
                current = current.next
            print()


# Example usage
dictionary = Dictionary(10)
dictionary.insert('apple', 3)
dictionary.insert('banana', 5)
dictionary.insert('cherry', 7)
dictionary.insert('date', 9)
dictionary.insert('grape', 11)
dictionary.display()

print('Value of key "banana":', dictionary.find('banana'))
print('Value of key "kiwi":', dictionary.find('kiwi'))

dictionary.delete('date')
dictionary.display()
