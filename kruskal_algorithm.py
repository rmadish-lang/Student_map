class DisjointSet:
    def __init__(self, vertices):
        self.parent = {vertex: vertex for vertex in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)
        if root1 != root2:
            self.parent[root2] = root1


def kruskal_algorithm(vertices, edges):
    # Sort edges by weight (distance)
    sorted_edges = sorted(edges, key=lambda edge: edge[2])
    
    disjoint_set = DisjointSet(vertices)
    mst = []  # Minimum Spanning Tree

    for u, v, weight in sorted_edges:
        if disjoint_set.find(u) != disjoint_set.find(v):
            disjoint_set.union(u, v)
            mst.append((u, v, weight))

    return mst


# --- Example Usage ---

cities = [
    "New York City", "Washington, DC", "Atlanta", "Miami", "Chicago",
    "Minneapolis", "Dallas", "New Orleans", "Denver", "Albuquerque",
    "Boise", "San Francisco", "Los Angeles", "Seattle", "Anchorage"
]

# (City1, City2, Distance)
edges = [
    ("New York City", "Washington, DC", 230),
    ("New York City", "Chicago", 790),
    ("Washington, DC", "Atlanta", 640),
    ("Atlanta", "Miami", 660),
    ("Atlanta", "Dallas", 780),
    ("Chicago", "Minneapolis", 410),
    ("Chicago", "Dallas", 920),
    ("Minneapolis", "Denver", 910),
    ("Dallas", "Albuquerque", 650),
    ("Dallas", "New Orleans", 510),
    ("Denver", "Albuquerque", 450),
    ("Denver", "Boise", 820),
    ("Albuquerque", "Los Angeles", 790),
    ("Boise", "San Francisco", 500),
    ("Boise", "Seattle", 500),
    ("Los Angeles", "San Francisco", 380),
    ("Los Angeles", "Seattle", 960)
]

# Build MST
mst = kruskal_algorithm(cities, edges)

# Print the Minimum Spanning Tree
print("Minimum Spanning Tree using Kruskal's Algorithm:")
for u, v, weight in mst:
    print(f"{u} -- {v} == {weight} miles")
