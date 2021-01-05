# Quick Sort
Quicksort is a popular sorting algorithm that is often faster in practice compared to other sorting algorithms. It utilizes a divide-and-conquer strategy to quickly sort data items by dividing a large array into two smaller arrays. It was developed by Charles Antony Richard Hoare (commonly known as C.A.R.
# Pseudocode
ALGORITHM QuickSort(arr, left, right)
    if left < right
        // Partition the array by setting the position of the pivot value 
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)

ALGORITHM Partition(arr, left, right)
    // set a pivot value as a point of reference
    DEFINE pivot <-- arr[right]
    // create a variable to track the largest index of numbers lower than the defined pivot
    DEFINE low <-- left - 1
    for i <- left to right do
        if arr[i] <= pivot
            low++
            Swap(arr, i, low)

     // place the value of the pivot location in the middle.
     // all numbers smaller than the pivot are on the left, larger on the right. 
     Swap(arr, right, low + 1)
    // return the pivot index point
     return low + 1

ALGORITHM Swap(arr, i, low)
    DEFINE temp;
    temp <-- arr[i]
    arr[i] <-- arr[low]
    arr[low] <-- temp

# Trace
sample array: [8,2,7,3]

# Pass 1
pivot=3
left=[2]
right=[8,7]
## It will take the right and compare it to the whole array starting from the left. Depending on the right it will divide the array into three parts. an array of values less than the right and it will be the new left, the right, and an array of values greater than the right which will be the new right.

# Pass 2
pivot=2
## It will repeat the same process for the left side.

# Pass 3
pivot=7
right=[8]
## It will repeat the same process for the right side.

# Pass 4
arr=[2,3,7,8]
## It will merge the sorted left, the pivot, and the sorted right into one array.

## Big O:

### time: O(n*log(n))

### space: O(1)




