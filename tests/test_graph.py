from data_structures_and_algorithms.Data_Structures.graph.graph import Graph

def test_graph():
    graph=Graph()
    assert graph.adjacency_list=={}
    graph.add_node(5)
    assert graph.adjacency_list=={5:{}}
    graph.add_node(10)
    graph.add_node(20)
    graph.add_node(30)
    graph.add_edge(10,20,9)
    assert graph.adjacency_list=={5: {}, 10: {20: 9}, 20: {10: 9}, 30: {}}
    graph.add_edge(10,30,9)
    graph.add_edge(5,10,9)
    graph.add_edge(5,20,1)
    graph.add_edge(5,30,3)
    assert graph.get_nodes()== [5, 10, 20, 30]
    assert graph.get_neighbours(5)=={10: 9, 20: 1, 30: 3}
    assert graph.size()==4
    
