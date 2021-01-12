from data_structures_and_algorithms.challenges.left_join.left_join import left_join
from data_structures_and_algorithms.Data_Structures.hashtable.hashtable import Hashmap

def test_simple_left_join():
    synonym=Hashmap(1024)
    antonyms=Hashmap(1024)
    synonym.add('fond','enamored')
    synonym.add('wrath','anger')
    antonyms.add('fond','averse')
    assert left_join(synonym, antonyms) == [['fond', 'enamored', 'averse'], ['wrath', 'anger', 'null']]
def test_no_common_keys():
    synonym=Hashmap(1024)
    antonyms=Hashmap(1024)
    synonym.add('fond','enamored')
    synonym.add('wrath','anger')
    antonyms.add('see','look')
    assert left_join(synonym, antonyms) == [['fond', 'enamored', 'null'], ['wrath', 'anger', 'null']]
def test_1st_dict_is_empty():
    synonym=Hashmap(1024)
    antonyms=Hashmap(1024)
    antonyms.add('see','look')
    assert left_join(synonym, antonyms) == []
def test_2nd_dictionary_empty():
    synonym=Hashmap(1024)
    antonyms=Hashmap(1024)
    synonym.add('fond','enamored')
    synonym.add('wrath','anger')
    assert left_join(synonym, antonyms) == [['fond', 'enamored', 'null'], ['wrath', 'anger', 'null']]
