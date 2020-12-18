from data_structures_and_algorithms.Data_Structures.stacks_and_queues.stacks_and_queues import Stack
from data_structures_and_algorithms.Data_Structures.queue_with_stacks.queue_with_stacks import PseudoQueue

def test_queue_with_stacks():
    q=PseudoQueue()
    assert q.dequeue()=='The stack is empty'
    q.enqueue(1)
    q.enqueue(2)
    assert q.dequeue()==1
    q.enqueue(5)
    q.enqueue(9)
    q.enqueue(3)
    assert q.dequeue()==2
    assert q.dequeue()==5
    assert q.stack1.peek()=='Stack is empty'
    assert q.stack2.peek()==9
    q.enqueue(8)
    assert q.stack1.peek()==8
    assert q.stack2.peek()=='Stack is empty'


