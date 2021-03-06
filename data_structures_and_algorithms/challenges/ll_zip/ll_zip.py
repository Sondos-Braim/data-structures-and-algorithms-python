from data_structures_and_algorithms.Data_Structures.linked_list.linked_list import LinkedList


def zipLists(list1,list2):
    list3=LinkedList()
    current1=list1.head
    current2=list2.head

    while current1!=None or current2!=None:
        
        if current1!=None:
            list3.append(current1.value)
            current1=current1.next
        if current2!=None:
            list3.append(current2.value)
            current2=current2.next

    return list3

if __name__ == "__main__":
    li=LinkedList()
    li2=LinkedList()
    li.insert(1)
    li.insert(2)
    li.insert(8)
    li2.insert(3)
    li2.insert(4)
    li2.insert(5)
    print(li)
    print(li2)
    print(zipLists(li,li2))
    
