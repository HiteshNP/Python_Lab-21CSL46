"""Develop a Python program to check whether a given number is palindrome or not and
also count the number of occurrences of each digit in the input number. """

num = input("Enter a number: ")

is_palindrome = num == num[::-1]
print(f"{num} is {'a palindrome.' if is_palindrome else 'not a palindrome.'}")

digit_occurrences = {digit: num.count(digit) for digit in num}
for digit, count in digit_occurrences.items():
    print(f"Occurrences of {digit}: {count}")
