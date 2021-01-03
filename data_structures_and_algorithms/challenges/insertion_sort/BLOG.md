list=[7,0,3]

## pass 1

min=0

i=0

temp=7

[7,0,3]-->[0,7,3]

- In the first pass through of the selection sort, we evaluate if there is a smaller number in the array than what is currently present in index 0. We find this smaller number right away in index 1. The minimum value gets updated to remember this index. At the end of the evaluation, the smaller number will be swapped with the current value in index i. This results in our smallest number of our array being placed first.

## pass 2

min=1

i=0

temp=0

[0,7,3]-->[0,3,7]

- The second pass through of the array only has one other index to evaluate. Since the last index value is larger than index 2, the two values will swap.


## pass 3

min=2

i=2

temp=3

[0,3,7]-->[0,3,7]

- On its final iteratation through the array, it will swap places with itself as it evaluates the value against itself.