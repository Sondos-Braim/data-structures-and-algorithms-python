def insertShiftArray(arr,val):
    newarr=[]
    arr1=arr[:int(len(arr)/2)]
    arr2=arr[int(len(arr)/2):]
    arr1.append(val)
    newarr=arr1+arr2  
    return newarr   
if __name__ == "__main__":
    print(insertShiftArray([2, 4, 6, 8], 5))