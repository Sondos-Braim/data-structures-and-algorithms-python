def reverseArray(arr):
    reversedList=arr[::-1]
    return reversedList

def issubset(arr1,arr2):
    for i in arr2:
        if i in arr1:
            continue
        else:
            return False
    return True

def printPairs(arr,  sum):
    pairs=[]
    for i in range(0, len(arr) ):
        for j in range(i + 1, len(arr) ):
            if (arr[i] + arr[j] == sum):
                new_arr=[arr[i],arr[j]]
                pairs.append(new_arr)
    return pairs
 
# Driver Code
if __name__ == "__main__":
    arr = [1,6,9,2,7,1,3]
    sum = 2
    print(printPairs(arr,  sum))
  

                


 