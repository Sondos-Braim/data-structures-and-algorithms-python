class Node:
    def __init__(self,value,nextNode=None):
        self.value=value
        self.next=nextNode

class Stack:
    def __init__(self):
        self.top=None

    def push(self, data):
        node = Node(data)
        if self.top:
            node.next = self.top
        self.top = node

    def pop(self):
        try:
            temp=self.top
            nextNode=self.top.next
            self.top.next=None
            self.top=nextNode
            return temp.value   
        except AttributeError:
            return 'The stack is empty'

    def peek(self):
        try:
            return self.top.value
        except AttributeError:
            return 'Stack is empty'
       
    def is_empty(self):
        if self.top:
            return False
        else:
            return True

class Queue:
    def __init__(self):
        self.front=None  
        self.rear=None  

    def enqueue(self, data):
        node = Node(data)

        if self.rear:
            self.rear.next = node
            self.rear = node
        else:
            self.front = node
            self.rear = node

    def dequeue(self):
        try:
            temp=self.front
            if self.front.next:
                nextNode=self.front.next
                self.front.next=None
                self.front=nextNode
            else:
                self.front=None
                self.rear=None
            return temp.value
        except AttributeError:
            return 'Queue is empty'
    # def dequeue(self):
    #     try:
    #         temp=self.front
    #         # nextNode=self.front.next
    #         if self.front.next:
    #             nextNode=self.front.next
    #             self.front.next=None
    #             self.front=nextNode
    #         else:
    #             self.front=None
    #         # self.front.next=None
    #         return temp
    #     except AttributeError:
    #         return 'Queue is empty'

    # def enqueue(self, data):
    #     node = Node(data)

    #     if self.rear:
    #         self.rear.next = node
    #         self.rear = node
    #     else:
    #         self.front = node
    #         self.rear = node

    # def dequeue(self):
    #     temp = self.front
    #     if self.is_empty():
    #         raise AttributeError ('Queue is empty')
    #     else:
            
    #         self.front = self.front.next
    #         temp.next = None
    #     if self.front == None:
    #         self.rear = None
    #     return temp

    def peek(self):
        try:
            return self.front.value
        except AttributeError:
            return 'Queue is empty'

    def is_empty(self):
        if self.front:
            return False
        else:
            return True



if __name__ == "__main__":
    stack = Stack()
    stack.push(5)
    stack.push(6)
    stack.push('cat')
    stack.pop()
    print(stack.peek())
    print(stack.is_empty())
    queue = Queue()
    queue.enqueue(4)
    queue.enqueue(5)
    queue.dequeue()
    print(queue.peek())
    print(queue.is_empty())