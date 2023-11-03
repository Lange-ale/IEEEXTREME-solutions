class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        i_root = self.find(i)
        j_root = self.find(j)
        if i_root == j_root:
            return False
        if self.rank[i_root] < self.rank[j_root]:
            self.parent[i_root] = j_root
        elif self.rank[i_root] > self.rank[j_root]:
            self.parent[j_root] = i_root
        else:
            self.parent[j_root] = i_root
            self.rank[i_root] += 1
        return True

n = int(input())
edges = []
cities = {}

for _ in range(n):
    city_i, city_j, cost = input().split()
    cost = int(cost)
    if city_i not in cities:
        cities[city_i] = len(cities)
    if city_j not in cities:
        cities[city_j] = len(cities)
    edges.append((cities[city_i], cities[city_j], cost))

# Sort edges based on cost
edges.sort(key=lambda x: x[2])

# Applying Kruskal's algorithm
uf = UnionFind(len(cities))
min_cost = 0
min_spanning_edges = []
edge_count = 0
for edge in edges:
    city_i, city_j, cost = edge
    if uf.union(city_i, city_j):
        min_cost += cost
        min_spanning_edges.append((city_i, city_j))
        edge_count += 1

if edge_count < len(cities) - 1:
    print(-1)
else:
    print(min_cost)
