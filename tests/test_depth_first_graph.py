from data_structures_and_algorithms.challenges.depth_first.depth_first import depth_first
from data_structures_and_algorithms.Data_Structures.graph.graph import Graph

def test_depth_first():
    graph=Graph()
    graph.add_node('A')
    graph.add_node('B')
    graph.add_node('C')
    graph.add_node('D')
    graph.add_node('E')
    graph.add_node('F')
    graph.add_node('G')
    graph.add_node('H')
    graph.add_edge('A','B')
    graph.add_edge('A','D')
    graph.add_edge('B','C')
    graph.add_edge('B','D')
    graph.add_edge('C','G')
    graph.add_edge('D','E')
    graph.add_edge('D','H')
    graph.add_edge('D','F')
    graph.add_edge('F','H')
    assert depth_first(graph,'A')==['A', 'B', 'C', 'G', 'D', 'E', 'H', 'F']
    assert depth_first(graph,'B')==['B', 'A', 'D', 'E', 'H', 'F', 'C', 'G']
    assert depth_first(graph,'C')==['C', 'B', 'A', 'D', 'E', 'H', 'F', 'G']
    assert depth_first(graph,'D')==['D', 'A', 'B', 'C', 'G', 'E', 'H', 'F']
    assert depth_first(graph,'E')==['E', 'D', 'A', 'B', 'C', 'G', 'H', 'F']




