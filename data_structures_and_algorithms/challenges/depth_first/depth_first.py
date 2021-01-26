from data_structures_and_algorithms.Data_Structures.graph.graph import Graph

def depth_first(graph,root):
    output=[]
    output.append(root)

    def _walk(node):
        nonlocal output
        neighbors=graph.adjacency_list[node].keys()
        for i in neighbors:
            if i not in output:
                output.append(i)
                _walk(i)
    _walk(root)
    return output




if __name__=="__main__":
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
    print(depth_first(graph,'E'))



