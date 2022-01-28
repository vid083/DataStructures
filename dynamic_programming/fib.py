# calculate the 40th number of the fibonacci sequence.

'''
1. Write a function 'fib(n)'that takes in a number as a argument.
    The function should return the nth number of the fibonacci sequence.

2. The 1st and 2nd number of the sequence is 1.
    To generate the next number of the sequence, we sum the previous two.

fib(n) : 1, 1, 2, 3, 5, 8, 13, 21, 34

'''

def fib(n):
    if n<=2:    return 1
    return fib(n-1) + fib(n-2)

print(fib(int(input("Enter the nth number to calculate: "))))