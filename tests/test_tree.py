import pytest
from data_structures_and_algorithms.Data_Structures.tree.tree import BinaryTree,BinarySearchTree,Node

def test_instantiate_and_single_root_node():
    bt = BinaryTree()
    actual = bt.preorder()
    expected = 'tree is empty'
    assert actual == expected
    bt.root=Node(5)
    assert bt.preorder()==[5]

def test_preorder(prep):
    assert prep.preorder() == [6,-1,10,5,7,3]
    assert prep.inOrder()== [10, -1, 6, 7, 5, 3]
    assert prep.postOrder()== [10, -1, 7, 3, 5, 6]

def test_binary_search(bst):
    assert bst.root.value == 4
    assert bst.root.left.value == -1
    assert bst.root.right.value == 9
    assert bst.root.left.right.value == 3
    assert bst.root.right.left.left.value == 5
    assert bst.contains(-1)==True
    assert bst.contains(4)== True
    assert bst.contains(9)==True
    assert bst.contains(5)== True
    assert bst.contains(1)== False

@pytest.fixture
def prep():
    bt = BinaryTree()
    bt.root = Node(6)
    bt.root.right = Node(5)
    bt.root.left = Node(-1)
    bt.root.right.left = Node(7)
    bt.root.left.left = Node(10)
    bt.root.right.right = Node(3)
    return bt

@pytest.fixture
def bst():
    bst = BinarySearchTree()
    bst.add(4)
    bst.add(9)
    bst.add(-1)
    bst.add(6)
    bst.add(3)
    bst.add(8)
    bst.add(5)
    return bst