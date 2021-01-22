from data_structures_and_algorithms.Data_Structures.stacks_and_queues.stacks_and_queues import Queue
class Node:
    def __init__(self, value):
        self.value = value


class Graph:

    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, value):
        node = Node(value).value
        self.adjacency_list[node] = {}

    def add_edge(self, start_node, end_node, weight=1):
        self.adjacency_list[start_node][end_node]=weight
        self.adjacency_list[end_node][start_node]=weight


    def get_nodes(self):
        arr=[]
        for i in self.adjacency_list.keys():
            arr.append(i)
        return arr


    def get_neighbours(self, node):
        return self.adjacency_list[node]

    def size(self):
        return len(self.adjacency_list.keys())

    def bfs(self, start_node):
        nodes = set() # O(1)
        breadth = Queue() # O(1)
        breadth.enqueue(start_node) # O(1)
        nodes.add(start_node)
        while breadth.front: # O(n)
            node = breadth.dequeue() # O(1)
            for n in self.adjacency_list[node].keys(): # O(n)
                if n not in nodes: # O(1)
                    breadth.enqueue(n) # O(1)
                    nodes.add(n)
        return nodes

# Adjacency_list = {n1:{n2:4,n4:5}, n2:{n1:4,n3:9}, n3:{n2:9}, n4:{n1:5,n3:9}, n5:{}}
if __name__ == "__main__":
    graph=Graph()
    graph.add_node(5)
    graph.add_node(10)
    graph.add_node(20)
    graph.add_node(30)
    graph.add_edge(10,20,9)
    print(graph.adjacency_list)

    graph.add_edge(10,30,9)
    graph.add_edge(5,10,9)
    graph.add_edge(5,20,1)
    graph.add_edge(5,30,3)
    print(graph.adjacency_list)
    print(graph.bfs(10))
    print(graph.get_nodes())
# Adjacency_list = {5:{10:9,20:1,30:3}, 10:{5:9,20:9,30:9}, 20:{5:1,10:9}, 30:{5:3,10:9}}
# {5,10,20,30}
#[10,5,20,30]
