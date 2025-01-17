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
        
        #check edge cases

        #if the start node is not in the graph, error

        if start not in self.graph:
            raise ValueError("Start node is not in the graph...")
        
        #if the end node is not in the graph, error

        if end != None and end not in self.graph:
            raise ValueError("End node is not in the graph...")

        # start the queue, list of visited nodes, and track parent nodes

        q = [start]
        visited = [start]
        parent_nodes = {start: None}

        #search the graph
        #a successor in the graph has an edge from the parent to the successor

        while len(q) > 0: #while the length of the queue is zero
            current = q.pop(0) #take the current node
            for neighbor in self.graph.successors(current):
                if neighbor not in visited: #if its an unsearched node
                    visited.append(neighbor) #visit the node
                    q.append(neighbor) #add the neighbor to the q
                    parent_nodes[neighbor] = current #add current as the parent of the neighbors

        # end node is specified and is visited in the search, return the shortest path

        if end != None and end in visited:
            shortest_path = []
            #start from the end and work back by calling its parents
            shortest_path_node = end
            while shortest_path_node != None: #while we aren't at the parent node
                shortest_path.append(shortest_path_node) #add the node
                shortest_path_node = parent_nodes[shortest_path_node] #move to its parent
            return shortest_path #return the direct path from the end to the beginning

        #no end node is specified, so return the bfs
        if end == None:
            return visited

        #if end node is specified but not visitied
        else:
            return None

        