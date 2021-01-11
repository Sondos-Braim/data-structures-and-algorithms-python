class Node:
    def __init__(self,value,nextV=None):
        self.value=value
        self.next=nextV
        self.index= 0
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
                if current.value==value:
                    self.head=Node(nValue,current)
                    break
                if current.next.value==value:
                    current.next=Node(nValue,current.next)
                    break
                else:
                    current=current.next
            
            self.size += 1
        except AttributeError:
            return 
      
    def insertAfter(self,value,nValue):
        try:
            current=self.head
            while current != None:
                if current.value==value:
                    current.next=Node(nValue,current.next)
                    break
                else:
                    current=current.next

            self.size += 1
        except AttributeError:
            return

    def index(self,k):
        current=self.head
        count=len(self)-1
        try:
            while current !=None:
                current.index=count
                if current.index==k:
                    return current.value
                current=current.next
                count-=1
        except AttributeError:
            return 

# def reverse(linkedlist):
#     if not linkedlist.head:
#         raise valueerror ('there is no head')
#     newList=LinkedList()
#     current=linkedlist.head
#     while current !=None:
#         if newList.head==None:
#             newList.head=Node(current.value,None)
#         else:
#             newList.head=Node(current.value,newList.head)
#         current=current.next
#     return newList

# def reverse(linkedlist):
#     if not linkedlist.head:
#          raise valueerror ('there is no head')
#     temp=None
#     current=linkedlist.head
#     while current !=None:
#         next = current.next
#         current.next = temp 
#         temp = current 
#         current =next
#         linkedlist.head = temp 
#     return linkedlist

def reverse(linkedlist):
    if not linkedlist.head:
         raise valueerror ('there is no head')
    temp=None
    current=linkedlist.head
    while current !=None:
        next = current.next
        current.next = temp
        temp = current
        linkedlist.head = current
        current =next
    return linkedlist

# [1,2,3]  current=1
#          next=2


if __name__ == "__main__":
    li=LinkedList()
    li.append(1)
    li.append(2)
    li.append(3)
    li.append(1)
    # print(li.includes(5))
    # print(li.includes(7))
    # print(li.includes(8))
    # print(li.includes(9))
    # print(li.includes(10))
    # print(li.includes(5))
    # print(li)
    # li.append(4)

    # li.append(5)
    # print(li)
    # li.insert(5)
    # print(li)
    li.insertBefore(1,1)
    li.insertBefore(2,4)
    li.insertBefore(3,5)
    li.insertBefore(1,5)

    print(li)
    # li.insertAfter(9,2)
    # li.insertAfter(8,6)
    # li.append(7)
    # li.append(9)

    # print(li)
    # print(reverse(li))
    # print(li.index(8))
    
  

# 1 -> 2 -> 3 -> Null
# ll = []


