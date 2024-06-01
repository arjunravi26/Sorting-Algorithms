def divide(arr):
    n = len(arr)
    
    if n <=1:
        return arr
    
    mid = n//2
    
    left_sub_array = divide(arr=arr[:mid])
    right_sub_array  = divide(arr=arr[mid:])
    
    return merge(left_sub_array,right_sub_array)

def merge(left,right):
    
    i,j = 0,0
    
    if len(left) < len(right):
        key = len(left) - 1
        
    else:
        key = len(right) - 1
    sorted_arr = [] 
    while key>=0:
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j+=1
        key = key - 1
    while i < len(left):
        sorted_arr.append(left[i])
        i += 1
    while j < len(right):
        sorted_arr.append(right[j])
        j += 1
        
    return sorted_arr
        
        
if __name__ == '__main__':
    arr = [1,4,5,2,10,9,11]
    sort = divide(arr)
    print(sort)
        
    
    
    