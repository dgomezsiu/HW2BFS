# write tests for bfs
import pytest
from search import graph

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    # function to initiate a graph object with tiny network adj list
    def test_tiny_network():
        return Graph('data/tiny_network.adjlist')
    
    #test traversal count by initiating tiny network adj graph

    def testing_traversal(test_graph):
        start_node = 'Luke Gilbert'
        expected_nodes = 31

        visited_nodes = test_tiny_network.bfs(start_node)
        assert len(visited_nodes) == expected_nodes, "Unexpected number of nodes"



def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    pass
