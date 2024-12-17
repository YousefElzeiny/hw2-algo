class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]  
        self.rank = [0] * n  

    def find(self, x):
      
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
      
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

def kruskal(n, edges):
    """
    n: Number of vertices
    edges: List of tuples (weight, u, v), where u and v are vertices connected by an edge
    """
   
    edges.sort()

    ds = DisjointSet(n)
    mst = []  
    mst_weight = 0

    for weight, u, v in edges:
        if ds.find(u) != ds.find(v): 
            ds.union(u, v)  
            mst.append((u, v, weight))  
            mst_weight += weight
    return mst, mst_weight

