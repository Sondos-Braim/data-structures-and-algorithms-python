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
            nextNode=self.top.next
            self.top.next=None
            self.top=nextNode
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
            nextNode=self.front.next
            self.front.next=None
            self.front=nextNode
        except AttributeError:
            return 'Queue is empty'

    def peek(self):
        try:
            return self.front.value
        except AttributeError:
            return 'Queque is empty'

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