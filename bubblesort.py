unorderArray = [1,8,6,25,7,3,89,0]

def bubbleSort(arr):
    for i in range(len(arr) -1):
        if arr[i] > arr[i+1]:
            aux = arr[i+1]
            arr[i+1] = arr[i]
            arr[i] = aux
    
    return arr

print(bubbleSort(unorderArray))        
            
            