from data_structures_and_algorithms.challenges.tree_intersection.tree_intersection import tree_intersection
from data_structures_and_algorithms.Data_Structures.tree.tree import BinaryTree,Node

def test_tree_intersection():
    tr1=BinaryTree()
    tr2 = BinaryTree()  
    assert tree_intersection(tr1,tr2)== [] 
    tr1.root = Node(5)
    assert tree_intersection(tr1,tr2)== []
    tr1.root.right = Node(10)
    tr1.root.left = Node(-2)
    tr1.root.right.left = Node(15)
    tr1.root.left.left = Node('string')
    tr2.root = Node(5)
    assert tree_intersection(tr1,tr2)== [5] 
    tr2.root.right = Node(11)
    tr2.root.left = Node(-2)
    tr2.root.right.left = Node(15)
    tr2.root.left.left = Node('string')
    assert tree_intersection(tr1,tr2)== [5, -2, 'string', 15]
