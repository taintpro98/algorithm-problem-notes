import queue


class Graph:
    def __init__(self, vertices) -> None:
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    def addEdge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def getShortestPath(self, start, end):
        myqueue = queue.Queue()
        visited = [False] * self.V
        distances = [-1] * self.V
        distances[start] = 0
        myqueue.put(start)
        while not myqueue.empty():
            el = myqueue.get()
            for next in self.adj[el]:
                if not visited[next]:
                    myqueue.put(next)
                    visited[next] = True
                    distances[next] = distances[el] + 1

        return distances[end]


g = Graph(10)
g.addEdge(0, 1)
g.addEdge(0, 3)
g.addEdge(1, 2)
g.addEdge(1, 4)
g.addEdge(1, 5)
g.addEdge(2, 6)
g.addEdge(3, 8)
g.addEdge(4, 5)
g.addEdge(4, 7)
g.addEdge(6, 7)
g.addEdge(7, 8)
g.addEdge(7, 9)
res = g.getShortestPath(0, 9)
print(res)  # 4
