class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printSolution(self, dist):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(node + 1, "\t\t", dist[node])

    def minDistance(self, dist, sptSet):
        min = 1e7
        for v in range(self.V):
            if dist[v] < min and not sptSet[v]:
                min = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, src):
        dist = [1e7] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
        for count in range(self.V):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and not sptSet[v] and \
                   dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
        self.printSolution(dist)

# Main program
g = Graph(6)
g.graph = [
    [0, 1, 0, 2, 0, 0],
    [1, 0, 5, 2, 0, 0],
    [0, 5, 0, 1, 0, 1],
    [2, 2, 1, 0, 3, 0],
    [0, 0, 2, 3, 0, 10],
    [0, 0, 1, 0, 10, 0]
]

g.dijkstra(0)  # The source vertex is 1, but array index starts from 0
