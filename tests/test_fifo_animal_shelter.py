from data_structures_and_algorithms.challenges.fifo_animal_shelter.fifo_animal_shelter import *
from data_structures_and_algorithms.Data_Structures.stacks_and_queues.stacks_and_queues import Queue,Node

def test_animal_shelter():
    shelter=AnimalShelter()
    cat1=Cat('jojo')
    cat2=Cat('tom')
    dog1=Dog('oscar')
    dog2=Dog('doo')
    shelter.enqueue(cat1)
    shelter.enqueue(dog1)
    shelter.enqueue(cat2)
    shelter.enqueue(dog2)
    assert shelter.dequeue('cat')=='jojo'
    assert shelter.dequeue('hamster')=='There are only cats and dogs'
    assert shelter.dequeue('dog')=='oscar'
    assert shelter.dequeue('dog')=='doo'
    assert shelter.dequeue('cat')=='tom'
    assert shelter.dequeue('cat')=='Queue is empty'
    assert shelter.dequeue('dog')=='Queue is empty'
