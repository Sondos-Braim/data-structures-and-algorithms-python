from data_structures_and_algorithms.challenges.array_shift.array_shift import insertShiftArray

def test_odd_array():
    array=[1,2,3,4,5]
    value=6
    actual = insertShiftArray(array,value)
    expected = [1,2,3,6,4,5]
    assert actual == expected

def test_even_array():
    array=[1,2,3,4]
    value=6
    actual = insertShiftArray(array,value)
    expected = [1,2,6,3,4]
    assert actual == expected    

def test_empty_array():
    array=[]
    value=6
    actual = insertShiftArray(array,value)
    expected=[6]
    assert actual == expected    

def test_empty_string():
    array=[1,2,3,4]
    value=''
    actual = insertShiftArray(array,value)
    expected= None
    assert actual == expected    




