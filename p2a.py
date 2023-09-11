"""Defined as a function F as Fn = Fn-1 + Fn-2. Write a Python program which accepts a
value for N (where N >0) as input and pass this value to the function. Display suitable
error message if the condition for input value is not followed."""


def F(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return F(number - 1) + F(number - 2)


n = int(input("Enter number of terms(where n>0):"))
if n < 0:
    print("Input value must be greater than 0")
else:
    print("Fibonacci series:", end=' ')
    for n in range(0, n):
        print(F(n), end=' ')
