class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def print_nodes(self, depth=0):
        print("  " * depth + self.name)
        for child in self.children:
            child.print_nodes(depth + 1)

# Create the book tree
book = Node("Book")

# Add chapters to the book
chapter1 = Node("Chapter 1")
chapter2 = Node("Chapter 2")
book.add_child(chapter1)
book.add_child(chapter2)

# Add sections to Chapter 1
section1_1 = Node("Section 1.1")
section1_2 = Node("Section 1.2")
chapter1.add_child(section1_1)
chapter1.add_child(section1_2)

# Add subsections to Section 1.1
subsection1_1_1 = Node("Subsection 1.1.1")
subsection1_1_2 = Node("Subsection 1.1.2")
section1_1.add_child(subsection1_1_1)
section1_1.add_child(subsection1_1_2)

# Add subsections to Section 1.2
subsection1_2_1 = Node("Subsection 1.2.1")
subsection1_2_2 = Node("Subsection 1.2.2")
section1_2.add_child(subsection1_2_1)
section1_2.add_child(subsection1_2_2)

# Add sections to Chapter 2
section2_1 = Node("Section 2.1")
chapter2.add_child(section2_1)

# Print the nodes of the book tree
book.print_nodes()
