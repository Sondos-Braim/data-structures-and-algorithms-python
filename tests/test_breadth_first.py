from data_structures_and_algorithms.Data_Structures.tree.tree import BinaryTree,Node
from data_structures_and_algorithms.challenges.breadth_tree.breadth import breadth_first

def test_breadth_first():
    bt = BinaryTree()
    assert breadth_first(bt)=="tree is empty"
    bt.root = Node(6)
    bt.root.right = Node(5)
    assert breadth_first(bt)==[6, 5]
    bt.root.left = Node(-1)
    assert breadth_first(bt)==[6, -1, 5]
    bt.root.right.left = Node(7)
    bt.root.left.left = Node(10)
    bt.root.right.right = Node(100)
    bt.root.right.right.left = Node(199)
    assert breadth_first(bt)==[6, -1, 5, 10, 7, 100, 199]

