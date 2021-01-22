class Queue:
    def __init__(self):
        self.front=None  
        self.rear=None  

    def enqueue(self, node):
        # node = Node(data)

        if self.rear:
            self.rear.next = node
            self.rear = node
        else:
            self.front = node
            self.rear = node

    def dequeue(self):
        temp=self.front
        if self.front.next:
            nextNode=self.front.next
            self.front.next=None
            self.front=nextNode
        else:
            self.front=None
            self.rear=None
        return temp

class Node:

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.next = None

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
    # def breadth_first(self):
    #     arr=[]
    #     if not self.root:
    #         return "tree is empty"
    #     arr.append(self.root)
    #     output=[]
    #     while arr:
    #         front=arr.pop(0)
    #         output.append(front.value)
    #         if front.left:
    #             arr.append(front.left)
    #         if front.right:
    #             arr.append(front.right)
    #     return output 

    def breadth_first(self):
        output=[]
        if not self.root:
            return "tree is empty"
        q=Queue()
        q.enqueue(self.root)
        while q.front:
            temp=q.dequeue()
            output.append(temp.value)
            if temp.left:
                q.enqueue(temp.left)
            if temp.right:
                q.enqueue(temp.right)
        return output

    # def breadth_first(self):
    # # INPUT  <-- root node
    # # OUTPUT <-- front node of queue to console

    # #Queue breadth <-- new Queue()
    #     node=self.root
    #     results =[]
    #     breadth = Queue()
    #     breadth.enqueue(node)
        
    #     try:
    #         while breadth.peek():
    #             front = breadth.dequeue()
    #             results.append(front.value)

    #             if front.left:
    #                 breadth.enqueue(front.left)

    #             if front.right:
    #                 breadth.enqueue(front.right)
    #     except AttributeError :
    #         pass
    #     return results

    # def add(self, value):
    #     if not self.root:
    #         self.root = Node(value)
    #     else:
    #         def _walk(node):
    #             if not node.left:
    #                 node.left = Node(value)
    #                 return
                    
    #             elif not node.right:
    #                 node.right = Node(value)
    #                 return
                
    #             _walk(node.right)
    #         _walk(self.root)
    def insert(self,key):
        temp=self.root
        if not temp:
            self.root = Node(key)
            return
        q = [] 
        q.append(temp)  
        while (len(q)): 
            temp = q[0] 
            q.pop(0) 
    
            if (not temp.left):
                temp.left = Node(key) 
                break
            else:
                q.append(temp.left) 
    
            if (not temp.right):
                temp.right = Node(key) 
                break
            else:
                q.append(temp.right) 
  


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

# def revert_tree(bt):
#     if not bt.root:
#         return None
#     def _walk(node):
#         if node.left and node.right:
#             left=node.left
#             node.left=node.right
#             node.right=left
#             _walk(node.left)
#             _walk(node.right)
#         if node.left and not node.right:
#             node.right=node.left
#             node.left=None
#         if node.right and not node.left:
#             node.left=node.right
#             node.right=None
#     _walk(bt.root)
#     return bt

def invert_tree(bt):
    if not bt.root:
        return "tree is empty"
    q=Queue()
    q.enqueue(bt.root)
    while q.front:       
        node=q.dequeue()
        if node.left and node.right:
            left_node=node.left
            node.left=node.right
            node.right=left_node
            q.enqueue(node.left)
            q.enqueue(node.right)
        if node.left and not node.right:
            node.right=node.left
            node.left=None
            q.enqueue(node.right)
        if node.right and not node.left:
            node.left=node.right
            node.right=None
            q.enqueue(node.left)
    return bt

# def invert_tree(bt):
#     if not bt.root:
#         return "tree is empty"
#     q=Queue()
#     while q.front:
#         node=q.dequeue()
#         if node.left and node.right:
#             leftNode=node.left
#             node.left=node.right
#             node.right=leftNode
#             q.enqueue(node.left)
#             q.enqueue(node.right)
#         if node.left and not node.right:
#             node.right=node.left
#             node.left=None
#             q.enqueue(node.right)
#         if node.right and not node.left:
#             node.left=node.right
#             node.right=None
#             q.enqueue(node.left)
#   return bt

def maxDepth(node): 
    if not node: 
        return 0 
    else : 
        if maxDepth(node.left) > maxDepth(node.right) : 
            return maxDepth(node.left) +1
        else: 
            return maxDepth(node.right) +1

# def is_bst(bt):
#     if not bt.root:
#             return 'empty tree'
#     node=bt.root
#     isBST=True
#     def _walk(node):
#         nonlocal isBST
#         if node.left:
#             if node.left.value>=node.value:
#                 isBST=False
#                 return isBST
#             else:
#                 _walk(node.left)
#         if node.right:
#             if node.right.value<node.value:
#                 isBST=False
#                 return isBST
#             else:
#                 _walk(node.right)
#         return isBST
 
#     return _walk(node)
def is_bst(bt):
    if not bt.root:
        return'empty'
    q = []
    boolen = True
    q.append(bt.root)
    while q :
        node = q.pop(0)
        if node.left  :
            if node.left.value> node.value:
                boolen= False
                return boolen
            else :
                q.append(node.left)
        if node.right  :
            if node.right.value < node.value:
                boolen= False
                return boolen
            else :
                q.append(node.right)
    return boolen
        
    #     if node.left:
    #         if node.left.value<node.value:
    #             return _walk(node.left)
    #         else:
    #             return False  
    #     if node.right:
    #         if node.right.value<node.value:
    #             return _walk(node.right)
    #         else:
    #             return False
        
    # _walk(bt.root)
    # return True
        

# def is_bst(tree):

#     def _walk(node):
#         if node == None:
#             return None
#         if node.left :
#             if node.left.value<node.value:
#                 _walk(node.left)
#             else:
#                 return False
#         if node.right:
#           if node.right.value>node.value:
#                _walk(node.right)
#               else:
#                    return False
#        return True
#     return _walk(tree.root)
def height(bt):
    pass
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
    
    # print(bt.root.value)
    # print(bt.root.left.value)
    # print(bt.root.right.value)
    # print(bt.root.left.left.value)
    # print(bt.root.left.right.value)
    # print(bt.root.right.left.value)
    # print(bt.root.right.right.value)

   
    bt.root = Node(6)   
    bt.root.left = Node(5)
    bt.root.right = Node(12)

    invert_tree(bt)
    print(bt.root.left.value)
    print(bt.root.right.value)

    # bt.root.right.right = Node(1)

    # bt.root.right.left = Node(8)
    # # print(is_bst(bt))

    # bt.root.right.right = Node(100)
    # bt.root.left.right = Node(99)
    # bt.root.right.right.left = Node(199)
    # bt.insert(2) #root
    # bt.insert(6) #left
    # bt.insert(9) #right
    # bt.insert(3) #left left
    # bt.insert(-1) #left right
    # bt.insert('hi') #right left
    # bt.insert(10) #right right
    # print(bt.breadth_first())
    # print(maxDepth(bt.root))
    # bt.add(5)
    # bt.add(6)
    # bt.add(8)
    # bt.add(11)
    # print(bt.root.value)
    # print(bt.root.left.value)
    # print(bt.root.right.value)
    # # print(bt.root.left.left.value)
    # print(bt.root.right.left.value)
    # print(bt.preorder())
    # print(bt.inOrder())
    # print(bt.postOrder())
  


