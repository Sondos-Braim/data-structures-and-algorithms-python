# Merge Sort
Merge sort is a method by which you break an unsorted array down into two smaller halves and so forth until you have a bunch of arrays of only two items. You sort each one, then merge each with another two-item array, then you merge the four-item arrays and so on all the way back up to a fully sorted array.
# Pseudocode
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length
           
    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1
            
        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left

# Trace
sample array: [8,2,7,3]

## Pass 1
left=[8,2] 

right=[7,3]
### In the first pass we split the array into left and right and save them into two variables.

## Pass 2
arr=[8,2], left=[8], right=[2]
### split the left into left and right.

## Pass 3
arr=[2,8]
### sort the right and left and merge them.

## Pass 4
arr=[7,3], left=[7], right=[3]
### split the left into left and right.

## Pass 5
arr=[3,7]
### sort the right and left and merge them.

## Pass 6
arr=[2,3,7,8]
### we will take the last sorted left and merge it with the last sorted right to have the sorted array.


## Big O:

### time: O(n*log(n))

### space: O(1)




