import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """
        # no end node, retur a list of nodes in BFS traversal order
        #take in a graph (self) and a starting node (start)
        if end is None:
            return list(nx.bfs_tree(self.graph, start))

        # yes end node, path available, return list of nodes with order of shortest path
        # take in graph (Self) and start node, and end node

        elif nx.has_path(self.graph, start, end):
            return nx.shortest_path(self.graph, start, end, method='bfs')
        
        # yes end node, but no path:
        else:
            return None