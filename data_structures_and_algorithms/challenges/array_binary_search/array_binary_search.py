def BinarySearch(arr,key):
    startIndex=0
    endIndex=len(arr)-1 
 
    while startIndex<=endIndex:
        midIndex=int((startIndex+endIndex)/2)
        if key>arr[midIndex]:
            startIndex=midIndex+1
        elif key<arr[midIndex]:
            endIndex=midIndex-1
        else:
            return midIndex
    return -1
            

if __name__ == "__main__":
    print(BinarySearch([1,2,3,4,3],5))