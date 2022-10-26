#this approach takes 100/100 points

class Node:
    def __init__(self, id, weight):
        self.id = id
        self.children_IDs = []
        self.parent = None
        self.depth = 0
        self.weight = weight

    def addChild(self, child):
        self.children_IDs.append(child)
        child.parent = self.id
        child.depth = self.depth + 1


def create_tree(root, adj, nodes):
    for i in adj[root.id]:
        if i != root.parent:
            root.addChild(nodes[i])
            create_tree(nodes[i], adj, nodes)


T = int(input())
for t in range(T):
    N = int(input())
    weights = [int(i) for i in input().split()]
    adj = {i:[] for i in range(N)}
    for i in range(N - 1):
        entry = input().split()
        v = int(entry[0]) - 1
        u = int(entry[1]) - 1
        adj[v].append(u)
        adj[u].append(v)
        
    nodes = [Node(i, weights[i]) for i in range(N)]
    root = nodes[0]
    create_tree(root, adj, nodes)

    Q = int(input())
    for q in range(Q):
        entry = input().split()
        op = int(entry[0])
        u = int(entry[1]) - 1
        v = int(entry[2]) - 1

        if op == 1:
            nodes[u].weight = v + 1
        else:  
            ans = 1
            while nodes[u].depth > nodes[v].depth:
                ans *= nodes[u].weight % 1000000007
                u = nodes[u].parent 
            while nodes[v].depth > nodes[u].depth:
                ans *= nodes[v].weight % 1000000007
                v = nodes[v].parent
            while u != v: 
                ans *= nodes[u].weight % 1000000007
                ans *= nodes[v].weight % 1000000007
                u = nodes[u].parent
                v = nodes[v].parent
            print(ans * nodes[u].weight % 1000000007)
