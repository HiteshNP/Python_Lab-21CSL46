""" Write a python program to find the best of two test average marks out of three test’s
marks accepted from the user"""

m1 = float(input("Enter the marks for test 1: "))
m2 = float(input("Enter the marks for test 2: "))
m3 = float(input("Enter the marks for test 3: "))
best_of_two = (m1 + m2 + m3 - min(m1, m2, m3)) / 2
print(f"The best of two test average marks out of three test’s marks accepted from the user is: {best_of_two}")
