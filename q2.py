import doctest
from enum import Enum
from typing import Callable

'''
In this question i chose to apply the Strategy pattern to solve the Connected Components problem.
The 2 possible algorithms are:
    - DFS = Depth First Search (DFSUtil)
    - BFS = Breadth First Search (BFSUtil)
    
Both of the algorithms are implemented in the Graph class.
Both of the algorithms are compatable with the connectedComponents function.

Each Graph holds within it a list of vertices and a list of edges (adjecency list).


'''


class OutputType(Enum):
    '''
    Enum class for the output type of the connectedComponents function.

    SIZE: returns the size of each connected component
    COMPONENTS: returns the connected components
    '''
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
        '''
        Constructor
        '''
        self.V = vertices
        # For each vertex create an empty list of adjacent vertices
        self.adj = [[] for _ in range(vertices)]

    def addEdge(self, u, v):
        '''
        Add an edge to the graph (undirected)
        '''
        self.adj[u].append(v)
        self.adj[v].append(u)

    def DFSUtil(self, v, visited):
        '''
        Recursive DFS algorithm

        Implemented by tracking all of the visited vertices in a list.

        returns a list of all the vertices in the connected component.
        '''
        visited[v] = True
        cc = [v]  # create a new list with the current vertex
        for i in self.adj[v]:
            # if the vertex is not visited, recursively call DFSUtil
            if not visited[i]:
                # extend the list with the returned list from the recursive call
                cc.extend(self.DFSUtil(i, visited))
        return cc

    def BFSUtil(self, v, visited):
        '''
        BFS algorithm

        Implemented using a queue. (by poppint the first element)
        '''
        queue = [v]
        cc = []
        while queue:  # while the queue is not empty
            s = queue.pop(0)  # pop the first element

            # if the vertex is not visited, mark it as visited and add it to the connected component
            if not visited[s]:
                cc.append(s)
                visited[s] = True

            # add all of the adjacent vertices to the queue
            for i in self.adj[s]:
                if not visited[i]:
                    queue.append(i)
        return cc

    def connectedComponents(self, algorithm: Callable = BFSUtil, output_type: OutputType = OutputType.SIZE):
        '''
        Returns the connected components of the graph.
        Arguments:
            algorithm: the algorithm to use (DFSUtil or BFSUtil)
            output_type: the output type (SIZE or COMPONENTS)

        '''
        visited = [False] * self.V  # Mark all the vertices as not visited
        cc = []  # list of connected components
        for v in range(self.V):
            # if the vertex is not visited, call the algorithm
            if not visited[v]:
                # append the returned list to the list of connected components
                cc.append(algorithm(v, visited))

        # if the output type is SIZE (or not provided), return the size of each connected component
        if output_type == OutputType.SIZE:
            return [len(x) for x in cc]
        # if the output type is COMPONENTS, return the connected components
        return cc


if __name__ == '__main__':
    doctest.testmod()
