from data_structures_and_algorithms.Data_Structures.stacks_and_queues.stacks_and_queues import *

def test_stack():
    stack = Stack()
    stack.push(5)
    stack.push(6)
    stack.push('cat')
    stack.pop()
    assert stack.peek()==6
    stack.is_empty()==False
    stack.pop()
    stack.pop()
    assert stack.peek()=='Stack is empty'

def test_queque():
    queue = Queue()
    queue.enqueue(4)
    queue.enqueue(5)
    queue.dequeue()
    assert queue.peek()==5
    queue.dequeue()
    assert queue.is_empty()==True
    assert queue.peek()=='Queque is empty'
