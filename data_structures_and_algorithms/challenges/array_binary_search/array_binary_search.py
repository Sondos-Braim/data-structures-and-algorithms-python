def BinarySearch(arr,key):
    startIndex=0
    endIndex=len(arr)-1
    if key not in arr:
        return -1
    else:    
        while startIndex<=endIndex:
            midIndex=int((startIndex+endIndex)/2)
            if key>arr[midIndex]:
                startIndex=midIndex+1
            elif key<arr[midIndex]:
                endIndex=midIndex-1
            else:
                return midIndex

            

