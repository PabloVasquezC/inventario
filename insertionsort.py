unorder_array = [4,7,1,33,89,24,6]

def insertion_sort(arr):
    for j in range(1, len(arr)):
        actual = arr[j]
        
        i = j-1
        while i >= 0 and arr[i] > actual:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = actual
    
    print(arr)   
    
insertion_sort(unorder_array)     
            