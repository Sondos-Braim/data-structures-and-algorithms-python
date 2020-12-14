from data_structures_and_algorithms.Data_Structures.stacks_and_queues.stacks_and_queues import Queue,Node
class AnimalShelter:
    def __init__(self):
        self.cats=Queue()
        self.dogs=Queue()

    def enqueue(self, data):
        if data.__class__.__name__=='Cat':
            self.cats.enqueue(data.name)
        elif data.__class__.__name__=='Dog':
            self.dogs.enqueue(data.name)
        else:
            return 'Only cats and dogs are allowed'

    def dequeue(self, pref):
        if pref=='cat':
            return self.cats.dequeue()
        elif pref=='dog':
            return self.dogs.dequeue()
        else:
            return 'There are only cats and dogs'

class Cat:
    def __init__(self,name):
        self.name=name

class Dog:
    def __init__(self,name):
        self.name=name


if __name__ == "__main__":
    shelter=AnimalShelter()
    cat1=Cat('jojo')
    cat2=Cat('tom')
    dog1=Dog('oscar')
    dog2=Dog('doo')
    shelter.enqueue(cat1)
    shelter.enqueue(dog1)
    shelter.enqueue(cat2)
    shelter.enqueue(dog2)
    print(shelter.dequeue('cat'))
    print(shelter.dequeue('hamster'))
    print(shelter.dequeue('dog'))
    print(shelter.dequeue('dog'))
    print(shelter.dequeue('cat'))


