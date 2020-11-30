#Import math library
import math

def insertShiftArray(arr,val):
    newarr=[]
    if val == '':
      print('none')
      return None
    if arr == []:
      newarr.append(val)
    for i in arr:
        if i==math.ceil(len(arr)/2)+1:
            newarr.append(val)
        newarr.append(i)
    print(newarr)    
    return newarr    
