from data_structures_and_algorithms.Data_Structures.tree.tree import BinaryTree,Node

def breadth_first(bt):
    arr=[]
    if not bt.root:
        return "tree is empty"
    arr.append(bt.root)
    output=[]
    while arr:
        front=arr.pop(0)
        output.append(front.value)
        if front.left:
            arr.append(front.left)
        if front.right:
            arr.append(front.right)
    return output  

if __name__ == "__main__":
    bt = BinaryTree()
    bt.root = Node(6)
    bt.root.right = Node(5)
    bt.root.left = Node(-1)
    bt.root.right.left = Node(7)
    bt.root.left.left = Node(10)
    bt.root.right.right = Node(100)
    bt.root.right.right.left = Node(199)
    print(breadth_first(bt))

