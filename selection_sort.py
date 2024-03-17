def selection_sort(arr):
    n = len(arr)
    for i in range(n):#this line starts a loop that iterates over each index of the array. The loop variable 
        min_index = i#At the beginning of each iteration of the outer loop, we assume that the element at index 
        for j in range(i+1, n):#Within the outer loop, another loop is started using the variable j. This loop iterates over the unsorted portion of the array, starting from i+1 to the end of the array.
            if arr[j] < arr[min_index]:#we compare the current element at index j with the element at the min_index. If the current element is smaller than the element 
                min_index = j#If the condition above is true, we update min_index to j
        arr[i], arr[min_index] = arr[min_index], arr[i]#After finding the smallest element in the unsorted portion of the array, we swap it with the element at index 

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
selection_sort(arr)
print("Sorted array:", arr)
