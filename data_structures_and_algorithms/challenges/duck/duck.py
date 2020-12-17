from data_structures_and_algorithms.Data_Structures.stacks_and_queues.stacks_and_queues import *

def DuckDuckGoose(listOfStrings, k): 
    queue=Queue()
    if len(listOfStrings)==0:
        return "list is empty"
    elif len(listOfStrings)==1:
        return listOfStrings[0]
   
    for i in listOfStrings:
        queue.enqueue(i)
    while queue.front.next:
        for i in range(k): 
            queue.enqueue(queue.dequeue())
        queue.dequeue()
    return queue.front.value

if __name__ == "__main__":
    print(DuckDuckGoose(['a','b','c','d','e'],2))
    print(DuckDuckGoose(['1','2','3','4','5','6'],3))









   