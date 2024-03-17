def factorial(n):
    if n == 0:#This line checks if the input n is equal to 0. If it is, #it immediately returns 1. This is because the factorial of 0 is defined to be 1.
        return 1
    else:
        return n * factorial(n-1)#If n is not equal to 0, then the else block is executed. This line recursively calls the factorial

# Example usage:
num = 5
print(f"Factorial of {num} is {factorial(num)}")
