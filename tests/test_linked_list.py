from data_structures_and_algorithms.Data_Structures.linked_list.linked_list import LinkedList
import pytest

def test_instantiate():
    li=LinkedList()
    assert li.head==None

def test_insert():
    li=LinkedList()
    li.insert(5)
    assert len(li)==1

def test_head():
    li=LinkedList()
    li.insert(5)
    li.insert(7)
    assert li.head.value==7

def test_insert_multiple_nodes():
    li=LinkedList()
    li.insert(5)
    li.insert(7)
    assert len(li)==2

def test_includes():
    li=LinkedList()
    li.insert(5)
    assert li.includes(5)=='True'
    assert li.includes(6)=='False'

def test_str():
    li=LinkedList()
    li.insert(5)
    li.insert(7)
    assert str(li)=='{7} -> {5} -> None'

def test_append():
    li=LinkedList()
    li.append(5)
    li.append(7) 
    assert len(li)==2
    assert li.head.value==5

def test_insertBefore():
    li=LinkedList()
    li.insert(5)
    li.insert(7)
    li.insertBefore(5,1)
    assert li.head.next.value==1

def test_insertAfter():
    li=LinkedList()
    li.insert(5)
    li.insert(7)
    li.insertAfter(7,1)
    assert li.head.next.value==1




