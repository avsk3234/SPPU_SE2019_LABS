def find(parent, node):
    if parent[node] == node:
        return node
    return find(parent, parent[node])


def union(parent, rank, node1, node2):
    root1 = find(parent, node1)
    root2 = find(parent, node2)

    if rank[root1] < rank[root2]:
        parent[root1] = root2
    elif rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        rank[root2] += 1


def kruskal(graph):
    # Sort the edges by their costs in ascending order
    edges = []
    for node in graph:
        for neighbor, cost in graph[node]:
            edges.append((node, neighbor, cost))
    edges.sort(key=lambda x: x[2])

    # Initialize the parent and rank arrays for disjoint set union
    parent = {}
    rank = {}
    for node in graph:
        parent[node] = node
        rank[node] = 0

    # Initialize the MST and total cost
    mst = []
    total_cost = 0

    # Perform Kruskal's Algorithm
    for edge in edges:
        node1, node2, cost = edge
        if find(parent, node1) != find(parent, node2):
            union(parent, rank, node1, node2)
            mst.append(edge)
            total_cost += cost

    return mst, total_cost


graph = {
    'City A': [('City B', 2), ('City C', 3)],
    'City B': [('City A', 2), ('City C', 1), ('City D', 4)],
    'City C': [('City A', 3), ('City B', 1), ('City D', 5)],
    'City D': [('City B', 4), ('City C', 5)]
}


# Call Kruskal's Algorithm to find the MST and total cost
mst, total_cost = kruskal(graph)

# Print the MST and total cost
print("Minimum Spanning Tree (MST):")
for edge in mst:
    print(f"{edge[0]} - {edge[1]}: {edge[2]}")
print(f"Total Cost: {total_cost}")
