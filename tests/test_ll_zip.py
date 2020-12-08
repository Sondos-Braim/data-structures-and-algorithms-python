from data_structures_and_algorithms.Data_Structures.linked_list.linked_list import LinkedList
from data_structures_and_algorithms.Data_Structures.ll_zip.ll_zip import zipLists

def test_list_zip():
    li=LinkedList()
    li2=LinkedList()
    li.insert(1)
    li.insert(2)
    li.insert(8)
    li2.insert(3)
    li2.insert(4)
    li2.insert(5)    
    assert str(zipLists(li,li2))=='{8} -> {5} -> {2} -> {4} -> {1} -> {3} -> None'
    assert len(li)+len(li2)==len(zipLists(li,li2))

def test_list_zip_not_equal_length():
    li=LinkedList()
    li2=LinkedList()
    li.insert(1)
    li.insert(2)
    li.insert(8)
    li2.insert(3)
    li2.insert(4)
    assert str(zipLists(li,li2))=='{8} -> {4} -> {2} -> {3} -> {1} -> None'
    assert len(li)+len(li2)==len(zipLists(li,li2))