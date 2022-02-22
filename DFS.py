"""
    DEPTH FIRST SEARCH ALGORITHM 
"""
from collections import defaultdict

class GRAPH:

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    ## add edges to the graph
    def AddEdges(self, u, v):
        self.graph[u].append(v)

    # helper function used by DFS - to mark the vertices traversed as visited
    def DFS_helper(self, v, visited):
        visited.append(v)
        print(v, end = ' ')

        # Recur for all vertices next to this node
        for i in self.graph[v]:
            if i not in visited:
                self.DFS_helper(i, visited) 

    # main DFS function
    def DFS(self,v): # starting node 'v'

        # create a set to store visited vertices
        visited = set()

        """
            If the graph is disconnected, then we need to run DFS on every vertex
        """
        for vertex in self.graph:
            if vertex not in visited:
                self.DFS_helper(v, visited) # this works fine when the graph is connected


if __name__ == '__main__':

    graph = GRAPH()

    graph.AddEdges(0,1)
    graph.AddEdges(0,2)

    graph.DFS(0)

    






