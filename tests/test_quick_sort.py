from data_structures_and_algorithms.challenges.quick_sort.quick_sort import quick_sort

def test_quick_sort():
    assert quick_sort([20,18,12,8,5,-2],0,5)==[-2,5,8,12,18,20]
    assert quick_sort([5,12,7,5,5,7],0,5)==[5,5,5,7,7,12]
    assert quick_sort([2,3,5,7,13,11],0,5)==[2,3,5,7,11,13]
