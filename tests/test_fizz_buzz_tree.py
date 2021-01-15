from data_structures_and_algorithms.Data_Structures.tree.tree import BinaryTree,Node
from data_structures_and_algorithms.challenges.fizz_buzz_tree.fizz_buzz_tree import fizzBuzz,FizzBuzzTree

def test_fizz_buzz():
    tree=BinaryTree()
    assert FizzBuzzTree(tree)=='tree is empty'
    tree.root=Node(5)
    assert FizzBuzzTree(tree).preorder()==['Buzz']
    tree.root.right=Node(8)
    assert FizzBuzzTree(tree).preorder()==['Buzz','8']
    tree.root.left=Node(6)
    assert FizzBuzzTree(tree).preorder()==['Buzz','Fizz','8']
    tree.root.right.left=Node(21)
    tree.root.right.right=Node(11)
    tree.root.left.left=Node(31)
    tree.root.left.right=Node(51)
    tree.root.right.left.right=Node(1)
    tree.root.right.right.left=Node(2)
    tree.root.left.left.right=Node(3)
    tree.root.left.right.left=Node(4)
    tree.root.left.right.right=Node(5) 
    tree.root.left.left.left=Node(15)
    assert FizzBuzzTree(tree).preorder()==['Buzz', 'Fizz', 'FizzBuzz', 'Buzz', '8', 'Fizz', 'Fizz', '1', '31', 'Fizz', '11', '2', '4']