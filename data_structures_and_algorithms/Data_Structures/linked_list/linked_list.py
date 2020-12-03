class Node:
    def __init__(self,value,nextV):
        self.value=value
        self.next=nextV

class LinkedList:
    def __init__(self):
        self.head=None
        self.size = 0

    def insert(self,data):
        if self.head==None:
            self.head=Node(data,None)
        else:
            self.head=Node(data,self.head)

        self.size += 1

    def includes(self,value):
        current=self.head
        while current != None:
            if current.value==value:
                return 'True' 
            else:
                current=current.next
        return 'False' 
    def __str__(self):
        result = ""
        node = self.head
        if not node:
            return '{}'
        while node:
            if node != None:
                result += f'{ { node.value  } }' + " -> "  
                node = node.next
            if node == None:
                result += "None" 
        return result  

    def __len__(self):
        return self.size
        
if __name__ == "__main__":
    li=LinkedList()
    li.insert(5)
    li.insert(7)
    li.insert(8)
    print(li.includes(5))
    print(li.includes(7))
    print(li.includes(8))
    print(li.includes(9))
    print(li.includes(10))
    print(li.includes(5))
    print(li)



