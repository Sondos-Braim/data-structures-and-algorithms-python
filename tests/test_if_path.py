from data_structures_and_algorithms.Data_Structures.graph.graph import Graph

def test_if_path():
    graph=Graph()
    graph.add_node(5)
    graph.add_node(10)
    graph.add_node(20)
    graph.add_node(30)
    graph.add_edge(10,20,9)
    graph.add_edge(10,30,9)
    graph.add_edge(5,10,9)
    graph.add_edge(5,20,1)
    graph.add_edge(5,30,3)
    assert graph.if_path(20,30)==False
    assert graph.if_path(5,30)==True