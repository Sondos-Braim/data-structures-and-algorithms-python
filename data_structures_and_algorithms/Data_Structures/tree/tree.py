class Node:

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinaryTree:

    def __init__(self):
        self.root = None

    def preorder(self):
        if not self.root:
            return 'tree is empty'
        output = []
        def _walk(node):
            output.append(node.value)
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)
        _walk(self.root)
        return output

    def inOrder(self):
        if not self.root:
            return 'tree is empty'
        output = []
        def _walk(node):           
            if node.left:
                _walk(node.left)
            output.append(node.value)
            if node.right:
                _walk(node.right)
        _walk(self.root)
        return output        

    def postOrder(self):
        if not self.root:
            return 'tree is empty'
        output = []
        def _walk(node):            
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)
            output.append(node.value)
        _walk(self.root)
        return output
    
    def find_maximum_value(self):
        if not self.root:
            return 'tree is empty'
        maximum_value=self.root.value
        def _walk(node):
            nonlocal maximum_value
            if node.value>maximum_value:
                maximum_value=node.value
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)
            return maximum_value
        return _walk(self.root)

    def add(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            def _walk(node):
                if not node.left:
                    node.left = Node(value)
                    return
                    
                if not node.right:
                    node.right = Node(value)
                    return
                _walk(node.right)
            _walk(self.root)



class BinarySearchTree(BinaryTree):

    def add(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            def _walk(node):
                if value < node.value:
                    if not node.left:
                        node.left = Node(value)
                        return
                    else:
                        _walk(node.left)
                else:
                    if not node.right:
                        node.right = Node(value)
                        return
                    else:
                        _walk(node.right)
            _walk(self.root)

    def contains(self, value):
        if not self.root:
            return False
        def _walk(node):
            if node:
                if node.value==value:
                    return True
                elif value<node.value:
                    return _walk(node.left)
                elif value>node.value:
                    return _walk(node.right) 
            return False           
        return _walk(self.root)

if __name__ == '__main__':

    # bst = BinarySearchTree()
    # bst.add(4)
    # bst.add(9)
    # bst.add(-1)
    # bst.add(6)
    # bst.add(3)
    # bst.add(8)
    # bst.add(5)

    # assert bst.root.value == 4
    # assert bst.root.left.value == -1
    # assert bst.root.right.value == 9
    # assert bst.root.left.right.value == 3
    # assert bst.root.right.left.left.value == 5
    # print('=====All passed======')
    # print(bst.contains(-1))
    # print(bst.contains(4))
    # print(bst.contains(9))
    # print(bst.contains(5))
    # print(bst.contains(1))
    bt = BinaryTree()
    # bt.root = Node(6)
    # bt.root.right = Node(5)
    # bt.root.left = Node(-1)
    # bt.root.right.left = Node(7)
    # bt.root.left.left = Node(10)
    # bt.root.right.right = Node(100)
    # bt.root.right.right.left = Node(99)
    # bt.root.right.right.left = Node(199)
    bt.add(5)
    bt.add(6)
    bt.add(8)
    bt.add(11)
    print(bt.root.right.left.value)
    print(bt.preorder())
    # print(bt.inOrder())
    # print(bt.postOrder())
  


