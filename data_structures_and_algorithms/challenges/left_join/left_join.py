from data_structures_and_algorithms.Data_Structures.hashtable.hashtable import Hashmap
def left_join(synonym, antonyms):
    output = [] 
    for linkedlist in synonym.map:
        if linkedlist == None :
            continue
        else:
            current = linkedlist.head   #O(n)
            while current:
                if  antonyms.contains(current.value[0]): #O(n)
                    output.append(current.value)
                    current.value.append(antonyms.get(current.value[0]))
                else:
                    output.append(current.value)
                    current.value.append('null') #O(n)
                current=current.next
    return output
if __name__ == "__main__":
    synonym=Hashmap(1024)
    antonyms=Hashmap(1024)
    synonym.add('could','enamored')
    synonym.add('cloud','anger')
    antonyms.add('fond','averse')
    print(left_join(synonym, antonyms))

