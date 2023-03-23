"""
ex_0_4.py

1. Write a Python module named ex_0_4.py that implements the following. 
Note that your script should include two functions and the script should not print anything.

*Tip: Run (or import) your Python

2. Define a function with name int_sum that takes one positional argument n.
 Use a loop inside the function to calculate the sum of the fist n non-zero integers.

"""
#1

def int_sum(n):
    total = 0 
    for i in range(1, n+1):
        total += i
    return total


#2
def odd_sum(n):
    count = 0
    total = 0
    i = 0
    while(count < n):
        i += 1
        if(i % 2 != 0):
            total += i
            count += 1
    return total