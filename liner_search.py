def linear_search(arr, x):
    for i in range(len(arr)):# start a loop that iterates over each index of the input array arr
        if arr[i] == x:#Within the loop, we check if the element at the current index i (i.e., arr[i]) is equal to the element x we are searching for.
            return i  
    return -1 

# Example usage:
arr = [5, 10, 15, 20, 25]
x = 15
result = linear_search(arr, x)
if result != -1:
    print(f"Element {x} found at index {result}")
else:
    print(f"Element {x} not found")
