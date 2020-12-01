from data_structures_and_algorithms.challenges.array_binary_search.array_binary_search import BinarySearch

def test_BinarySearch():
    arr=[1,2,3,4,5,6,7,8,9,10]
    key=10
    actual=BinarySearch(arr,key)
    expected=9
    assert actual==expected

def test_BinarySearch_odd():
    arr=[1,2,3,4,5,6,7,8,9]
    key=9
    actual=BinarySearch(arr,key)
    expected=8
    assert actual==expected

def test_not_in_array():
    arr=[1,2,3,4,5,6,7,8,9]
    key=10
    actual=BinarySearch(arr,key)
    expected=-1
    assert actual==expected


