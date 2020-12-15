from data_structures_and_algorithms.Data_Structures.stacks_and_queues.stacks_and_queues import Stack

def multi_bracket_validation(input):
    stack=Stack()
    for i in input:
        if i=='{' or i=='[' or i=='(':
            stack.push(i) 
        elif i=='}':
            if stack.peek()=='{':
                stack.pop()
            else:
                return False
        elif i==']':
            if stack.peek()=='[':
                stack.pop()
            else:
                return False
        elif i==')':
            if stack.peek()=='(':
                stack.pop()
            else:
                return False
    if stack.top:
        return False
    else:
        return True
            
 
if __name__ == "__main__":
    print(multi_bracket_validation('[hi]I{am}s(o)[n]dos'))