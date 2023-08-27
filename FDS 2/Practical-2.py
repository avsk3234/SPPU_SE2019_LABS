class Set:
    def __init__(self):
        self.collection = []

    def add(self, element):
        if element not in self.collection:
            self.collection.append(element)

    def remove(self, element):
        if element in self.collection:
            self.collection.remove(element)

    def contains(self, element):
        return element in self.collection

    def size(self):
        return len(self.collection)

    def iterator(self):
        return iter(self.collection)

    def intersection(self, other_set):
        intersection_set = Set()
        for element in self.collection:
            if other_set.contains(element):
                intersection_set.add(element)
        return intersection_set

    def union(self, other_set):
        union_set = Set()
        union_set.collection = self.collection.copy()
        for element in other_set.collection:
            if element not in self.collection:
                union_set.add(element)
        return union_set

    def difference(self, other_set):
        difference_set = Set()
        for element in self.collection:
            if not other_set.contains(element):
                difference_set.add(element)
        return difference_set

    def subset(self, other_set):
        for element in self.collection:
            if not other_set.contains(element):
                return False
        return True

# Create two sets
set1 = Set()
set2 = Set()

# Add elements to set1
set1.add(1)
set1.add(2)
set1.add(3)

# Add elements to set2
set2.add(2)
set2.add(3)
set2.add(4)

# Test remove() method
set1.remove(2)

# Test contains() method
print(set1.contains(1))  # True
print(set1.contains(2))  # False

# Test size() method
print(set1.size())  # 2

# Test iterator() method
for element in set1.iterator():
    print(element)  # 1, 3

# Test intersection() method
intersection_set = set1.intersection(set2)
for element in intersection_set.iterator():
    print(element)  # 3

# Test union() method
union_set = set1.union(set2)
for element in union_set.iterator():
    print(element)  # 1, 3, 4

# Test difference() method
difference_set = set1.difference(set2)
for element in difference_set.iterator():
    print(element)  # 1

# Test subset() method
print(set1.subset(set2))  # False
