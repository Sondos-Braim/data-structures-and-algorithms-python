from data_structures_and_algorithms.Data_Structures.tree.tree import BinaryTree, Node
def tree_intersection(tree1,tree2):
    output=[]
    if tree1.root and tree2.root:
        list1=tree1.preorder()
        list2=tree2.preorder()       
        list2=set(list2)
        for i in list1:
            if i in list2:
                output.append(i)
    return output

if __name__ == "__main__":
    # tree1=BinaryTree()
    # tree2=BinaryTree()
    # tree1.root= Node(5)
    # tree1.root.left= Node(7)
    # tree1.root.right= Node(-1)
    # tree2.root= Node(4)
    # tree2.root.left= Node(7)
    # tree2.root.right= Node(-1)
    tr1=BinaryTree()
    tr2 = BinaryTree()
    tr1.root = Node(5)
    tr1.root.right = Node(10)
    tr1.root.left = Node(-2)
    tr1.root.right.left = Node(15)
    tr1.root.left.left = Node(17)
    tr2.root = Node(5)
    tr2.root.right = Node(11)
    tr2.root.left = Node(-2)
    tr2.root.right.left = Node(15)
    tr2.root.left.left = Node(111)
    print(tree_intersection(tr1,tr2))