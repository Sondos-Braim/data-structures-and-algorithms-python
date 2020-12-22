from data_structures_and_algorithms.Data_Structures.tree.tree import BinaryTree,Node
def fizzBuzz(node):
    if node:
        if node.value%3==0 and node.value%5==0:
            return'FizzBuzz'
        elif node.value%3==0:
            return'Fizz'
        elif node.value%5==0:
            return'Buzz'
        else:
            return str(node.value)

def FizzBuzzTree(bt):
    try:
        new_tree=BinaryTree()
        def _walk(node):
            new_tree.add(fizzBuzz(node))       
            if node.left:           
                _walk(node.left)
            if node.right:
                _walk(node.right)
            return new_tree
        return _walk(bt.root)
    except:
        return "tree is empty"

if __name__ == "__main__":
    tree=BinaryTree()
    tree.root=Node(5)
    tree.root.right=Node(8)
    tree.root.left=Node(6)
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
   
    

    print(tree.preorder())
    print (FizzBuzzTree(tree).preorder())