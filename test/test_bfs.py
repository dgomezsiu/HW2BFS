# write tests for bfs
import pytest
import networkx as nx
from search import graph

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """

    #starting at the first given node in the file, is the length of the number of nodes correct?
    test_graph = graph.Graph('data/tiny_network.adjlist')
    bfs_test_graph = test_graph.bfs('Luke Gilbert')
    assert len(bfs_test_graph) == 30

    #use nx package to build bfs and compare graphs to make sure they are the same length
    realgraph_bfs = list(nx.bfs_tree(test_graph.graph, 'Luke Gilbert').nodes())
    assert len(bfs_test_graph) == len(bfs_test_graph)

    #check if the nodes are traversed in the same order
    assert realgraph_bfs == bfs_test_graph


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

    test_graph = graph.Graph('data/citation_network.adjlist')
    
    #test if the path between two nodes is shortest using nx package
    assert len(test_graph.bfs("Yin Shen", "Matthew Spitzer")) == len(list(nx.shortest_path(test_graph.graph, "Yin Shen", "Matthew Spitzer")))

    #test if the raise error is correct. Elmo is not in the graph
    with pytest.raises(ValueError):
        test_graph.bfs('Yin Shen', "Elmo")

    #return none when unconnected nodes are called
    assert test_graph.bfs('Reza Abbasi-Asl', 'Hao Li') == None