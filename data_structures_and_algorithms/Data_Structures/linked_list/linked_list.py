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

def palindrome(linkedlist):
    save=LinkedList()
    if not linkedlist.head:
         raise valueerror ('there is no head')
    temp=None
    current=linkedlist.head
    while current !=None:
        save.append(current.value)
        next = current.next
        current.next = temp
        temp = current
        linkedlist.head = current
        current =next
    if save==linkedlist:
        return True
    else:
        return False

# [1,2,3]  current=1
#          next=2

# def intersection(li1,li2):
#     head1=li1.head
#     head2=li2.head
#     while head1.value != head2.value:
#         if head1:
#             # print(head1.value)
#             head1=head1.next
#         else:
#             print('hiiiiiiiiiii')
#             head1=li2.head
#         if head2:
#             head2=head2.next
#         else:
#             print('hiiiiiiiiiiiiiiiiiii')
#             head2=li1.head
#     return head1.value
def getIntersectionNode( headA, headB):
    curA,curB = headA,headB
    lenA,lenB = 0,0
    while curA is not None:
        lenA += 1
        curA = curA.next
    while curB is not None:
        lenB += 1
        curB = curB.next
    curA,curB = headA,headB
    if lenA > lenB:
        for i in range(lenA-lenB):
            curA = curA.next
    elif lenB > lenA:
        for i in range(lenB-lenA):
            curB = curB.next
    while curB.value != curA.value:
        curB = curB.next
        curA = curA.next
    return curA.value

def print_middle(llist):
    current = llist.head
    length = 0
    while current:
        current = current.next
        length = length + 1
    current = llist.head
    for i in range((length - 1)//2):
        current = current.next
    if current:
        if length % 2 == 0:
            return('The two middle elements are {} and {}.'
                .format(current.data, current.next.data))
        else:
            return('The middle element is {}.'.format(current.data))
    else:
        return('The list is empty.')

def odd_then_even(ll):
    odd=ll.head
    even=ll.head.next
    list2=LinkedList()
    while odd:
        list2.append(odd.value)
        for i in range(2):
            if odd:
                odd=odd.next
            else:
                odd=None
    while even:
        list2.append(even.value)
        for i in range(2):
            if even:
                even=even.next
            else:
                even=None      
    return list2

if __name__ == "__main__":
    li1=LinkedList()
    li1.append(4)
    li1.append(-9)
    li1.append(1)
    li1.append(2)
    li1.append(3)
    li1.append(4)
    print(odd_then_even(li1))
    # li2=LinkedList()
    # li2.append(99)
    # li2.append(1)
    # li2.append(2)
    # li2.append(3)
    # li2.append(4)
    # print(li1)
    # # print(li2)
    # print(palindrome(li1))  

    # reverse(li.head)

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
    # li.insertBefore(1,1)
    # li.insertBefore(2,4)
    # li.insertBefore(3,5)
    # li.insertBefore(1,5)

    # print(li)
    # li.insertAfter(9,2)
    # li.insertAfter(8,6)
    # li.append(7)
    # li.append(9)

    # print(li)
    # print(reverse(li))
    # print(li.index(8))
    
  

# 1 -> 2 -> 3 -> Null
# ll = []


