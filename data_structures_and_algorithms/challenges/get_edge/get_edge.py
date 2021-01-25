from data_structures_and_algorithms.Data_Structures.graph.graph import Graph

def get_edge(graph,cities):
    sum=0
    for i in range(len(cities)):
        neighbors=graph.adjacency_list[cities[i]].keys()
        if i+1==len(cities):
            break
        if cities[i+1] in neighbors:
            sum+=graph.adjacency_list[cities[i+1]][cities[i]]
        else:
            return 0,False
    return True,sum


if __name__=='__main__':
    cities=['Pandora','Metroville', 'Narnia', ]
    graph=Graph()
    graph.add_node('Pandora')
    graph.add_node('Metroville')
    graph.add_node('Narnia')
    graph.add_node('Naboo')
    graph.add_node('Arendelle')
    graph.add_node('Monstropolis')
    graph.add_edge('Pandora','Arendelle',150)
    graph.add_edge('Pandora','Metroville',82)
    graph.add_edge('Metroville','Narnia',37)
    print(graph.adjacency_list)
    print(get_edge(graph,cities))
