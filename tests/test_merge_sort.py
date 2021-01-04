from data_structures_and_algorithms.challenges.merge_sort.merge_sort import *

def test_merge_sort():
    assert merge_sort([20,18,12,8,5,-2])==[-2,5,8,12,18,20]
    assert merge_sort([5,12,7,5,5,7])==[5,5,5,7,7,12]
    assert merge_sort([2,3,5,7,13,11])==[2,3,5,7,11,13]
