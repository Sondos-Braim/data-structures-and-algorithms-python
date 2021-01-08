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

# def binary_search(arr,value):
  
#   while len(arr)>0:
#     mid_index=int(len(arr)/2) 
#     if arr[mid_index]==value: 
#       return arr[mid_index]
#     elif arr[mid_index]>value:
#       new_arr=arr[:mid_index]
#       return binary_search(new_arr,value)
#     else:
#       new_arr=arr[mid_index:]
#       return binary_search(new_arr,value)  
#   return "value not found"

# print(binary_search([5,9,13,33],33))
            

if __name__ == "__main__":
    print(BinarySearch([1,2,3,4,3],5))
