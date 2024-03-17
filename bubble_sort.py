def bubble_sort(arr):#define a function
    n = len(arr)# calculate array length
    
    for i in range(n):#start sa loop iterate all the element
        
        for j in range(0, n-i-1):#Within the outer loop, another loop is started using the variable j. This loop iterates over the unsorted portion of the array.
            
            
            if arr[j] > arr[j+1]:#This condition checks if the current element (arr[j]) is greater than the next element (arr[j+1]). If this condition is true, it means that the elements are in the wrong order, and they need to be swapped.
                arr[j], arr[j+1] = arr[j+1], arr[j]#If the condition above is true, this line swaps the elements 


arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array:", arr)
