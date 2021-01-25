from data_structures_and_algorithms.Data_Structures.graph.graph import Graph
from data_structures_and_algorithms.challenges.get_edge.get_edge import get_edge

def test_get_edge():
    cities=['Pandora','Metroville', 'Narnia', ]
    graph=Graph()
    graph.add_node('Pandora')
    graph.add_node('Metroville')
    graph.add_node('Narnia')
    graph.add_node('Naboo')
    graph.add_node('Arendelle')
    graph.add_node('Monstropolis')
    assert get_edge(graph,cities)==(0,False)
    graph.add_edge('Pandora','Arendelle',150)
    graph.add_edge('Pandora','Metroville',82)
    graph.add_edge('Metroville','Narnia',37)
    assert get_edge(graph,cities)==(True,119)
    places=['Monstropolis','Narnia']
    assert get_edge(graph,places)==(0,False)
    graph.add_edge('Monstropolis','Narnia',210)
    assert get_edge(graph,places)==(True,210)






