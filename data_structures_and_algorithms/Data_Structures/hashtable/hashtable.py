from data_structures_and_algorithms.Data_Structures.linked_list.linked_list import LinkedList, Node
class Hashmap:
    def __init__(self, size):
        self.size = size
        self.map = [None]*size

    def add(self, key, value):
        idx = self.get_hash(key)
        if not self.map[idx]:
            self.map[idx] = LinkedList()
        self.map[idx].insert([key, value])

    # def add(self, key, value):
    #     index = self.hash(key)
    #     if self.map[index] == None:
    #         self.map[index] = Linkedlist()
    #         self.map[index].add([key, value])
    #     else:
    #         self.map[index].add([key,value])

    def get(self, key):
        idx = self.get_hash(key)
        if self.map[idx]:
            current = self.map[idx].head
            while current:
                if current.value[0] == key :
                    return current.value[1]
                current = current.next
        else:
            return None
    def contains(self,key):
        if  self.map[self.get_hash(key)]:
            return True
        else:
            return False


    # def find(self, key):
    #     try:
    #         idx = self.get_hash(key)
    #         current=self.map[idx].head
    #         while current.value:
    #             if key in current.value:
    #                 return current.value[key]
    #             current=current.next
    #             if current==None:
    #                 break
    #     except:
    #         return None
        

    # def contains(self, key):
    #     try:
    #         idx = self.get_hash(key)
    #         current=self.map[idx].head
    #         while current.value:
    #             if key in current.value:
    #                 return True
    #             current=current.next
    #             if current==None:
    #                 break
    #     except:
    #         return False
        


    def get_hash(self, key):
        ascii_total = 0
        for ch in key:
            ascii_total += ord(ch)
        hashed = ascii_total * 17
        hashed = hashed % self.size
        return hashed



if __name__=='__main__':
    things = Hashmap(1024)
    things.add('name', 'Ahmad')
    things.add('color', 'red')
    things.add('num', 3)
    things.add('cat', 'kittie')
    things.add('act', 'good')
    print(things.map[things.get_hash('act')].head.next.value)

 