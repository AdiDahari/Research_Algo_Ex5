import doctest
from enum import Enum
from typing import Callable


class OutputType(Enum):
    SIZE = 1
    COMPONENTS = 2


class Graph:
    '''
    TESTS:
    >>> g = Graph(5)
    >>> g.addEdge(1, 0)
    >>> g.addEdge(2, 3)
    >>> g.addEdge(3, 4)
    >>> print(g.connectedComponents(g.DFSUtil, OutputType.SIZE))
    [2, 3]
    >>> print(g.connectedComponents(g.BFSUtil, OutputType.SIZE))
    [2, 3]
    >>> print(g.connectedComponents(g.DFSUtil, OutputType.COMPONENTS))
    [[0, 1], [2, 3, 4]]
    >>> print(g.connectedComponents(g.BFSUtil, OutputType.COMPONENTS))
    [[0, 1], [2, 3, 4]]

    >>> g = Graph(10)
    >>> g.addEdge(1, 0)
    >>> g.addEdge(2, 3)
    >>> g.addEdge(3, 4)
    >>> g.addEdge(5, 6)
    >>> g.addEdge(6, 7)
    >>> g.addEdge(7, 8)
    >>> g.addEdge(8, 0)
    >>> print(g.connectedComponents(g.DFSUtil, OutputType.SIZE))
    [6, 3, 1]
    >>> print(g.connectedComponents(g.BFSUtil, OutputType.SIZE))
    [6, 3, 1]
    >>> print(g.connectedComponents(g.DFSUtil, OutputType.COMPONENTS))
    [[0, 1, 8, 7, 6, 5], [2, 3, 4], [9]]
    >>> print(g.connectedComponents(g.BFSUtil, OutputType.COMPONENTS))
    [[0, 1, 8, 7, 6, 5], [2, 3, 4], [9]]
    '''

    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    def addEdge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def DFSUtil(self, v, visited):
        visited[v] = True
        cc = [v]
        for i in self.adj[v]:
            if not visited[i]:
                cc.extend(self.DFSUtil(i, visited))
        return cc

    def BFSUtil(self, v, visited):
        queue = [v]
        cc = []
        while queue:
            s = queue.pop(0)
            if not visited[s]:
                cc.append(s)
                visited[s] = True
            for i in self.adj[s]:
                if not visited[i]:
                    queue.append(i)
        return cc

    def connectedComponents(self, algorithm: Callable = BFSUtil, output_type: OutputType = OutputType.SIZE):
        visited = [False] * self.V
        cc = []
        for v in range(self.V):
            if not visited[v]:
                cc.append(algorithm(v, visited))

        if output_type == OutputType.SIZE:
            return [len(x) for x in cc]

        return cc


if __name__ == '__main__':
    doctest.testmod()
