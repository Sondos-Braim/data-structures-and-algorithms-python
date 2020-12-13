from data_structures_and_algorithms.Data_Structures.stacks_and_queues.stacks_and_queues import Stack

class PseudoQueue:
    def __init__(self):
        self.stack1=Stack()  
        self.stack2=Stack()

    def enqueue(self,val):
        while self.stack2.top:
            self.stack1.push(self.stack2.pop())
        self.stack1.push(val)

    def dequeue(self):
        while self.stack1.top:
            self.stack2.push(self.stack1.pop())
        return self.stack2.pop()
      

if __name__ == "__main__":
    q=PseudoQueue()
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())

