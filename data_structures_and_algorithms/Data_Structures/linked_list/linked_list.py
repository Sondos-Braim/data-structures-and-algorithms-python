class Node:
    def __init__(self,value,nextV=None):
        self.value=value
        self.next=nextV

class LinkedList:
    def __init__(self):
        self.head=None
        self.size = 0

    def insert(self,data):
        if self.head==None:
            self.head=Node(data)
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
            result += f"{ { node.value  } } -> "  
            node = node.next
            if node == None:
                        result += "None" 
        return result  

    def __len__(self):
        return self.size

    def append(self,value):
        if self.head==None:
            self.head=Node(value)
        else:
            current=self.head
            while current.next != None:
                current=current.next
            current.next=Node(value)

        self.size += 1


    def insertBefore(self,value,nValue):
        try:
            current=self.head
            while current.next != None:
                if current.next.value==value:
                    current.next=Node(nValue,current.next)
                    break
                else:
                    current=current.next
            
            self.size += 1
        except AttributeError:
            return 
      


    def insertAfter(self,value,nValue):
        current=self.head
        while current != None:
            if current.value==value:
                current.next=Node(nValue,current.next)
                break
            else:
                current=current.next

        self.size += 1

        





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
    li.append(9)
    print(li)
    li.insert(5)
    print(li)
    li.insertBefore(9,1)
    li.insertBefore(5,1)
    li.insertAfter(9,2)
    li.insertAfter(8,6)
    li.append(5)
    print(li)

  


