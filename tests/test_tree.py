import pytest
from data_structures_and_algorithms.Data_Structures.tree.tree import BinaryTree,BinarySearchTree,Node

def test_instantiate_and_single_root_node():
    bt = BinaryTree()
    actual = bt.preorder()
    expected = 'tree is empty'
    assert actual == expected
    bt.root=Node(5)
    assert bt.preorder()==[5]

def test_traversal(prep):
    assert prep.preorder() == [6,-1,10,5,7,3]
    assert prep.inOrder()== [10, -1, 6, 7, 5, 3]
    assert prep.postOrder()== [10, -1, 7, 3, 5, 6]
    prep.root.right.right.right = Node(9)
    assert prep.preorder() == [6, -1, 10, 5, 7, 3, 9]
    assert prep.inOrder()== [10, -1, 6, 7, 5, 3, 9]
    assert prep.postOrder()== [10, -1, 7, 9, 3, 5, 6]

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

def test_find_maximum_value(prep):
    assert prep.find_maximum_value()==10
    prep.root.right.right.right = Node(99)
    assert prep.find_maximum_value()==99
    new_tree=BinaryTree()
    assert new_tree.find_maximum_value()=='tree is empty'
    new_tree.root = Node(8)
    new_tree.root.right = Node(5)
    new_tree.root.left = Node(-1)
    assert new_tree.find_maximum_value()== 8

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