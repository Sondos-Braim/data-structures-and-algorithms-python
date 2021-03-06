from data_structures_and_algorithms.Data_Structures.hashtable.hashtable import Hashmap

def test_hash_table():
    things = Hashmap(1024)
    things.add('name', 'Ahmad')
    things.add('color', 'red')
    things.add('num', 3)
    things.add('cat', 'kittie')
    things.add('act', 'good') #this will cause collision
    assert things.contains('name') == True
    assert things.contains('color') == True
    assert things.contains('num') == True
    assert things.contains('act') == True 
    assert things.contains('cat') == True
    assert things.contains('game') == False
    assert things.get('name') == 'Ahmad'
    assert things.get('color') == 'red'
    assert things.get('num') == 3
    assert things.get('game') == None
    assert things.get('cat') == 'kittie'
    assert things.get('act') == 'good'