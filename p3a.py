"""Write a Python program that accepts a sentence and find the number of words, digits,
uppercase letters and lowercase letters."""

sentence = input("Enter a sentence:")
wordlist = sentence.split()
digits = 0
upper = 0
lower = 0

for char in sentence:
    if char.isdigit():
        digits += 1
    elif char.isupper():
        upper += 1
    elif char.islower():
        lower += 1

print("Number of words:", len(wordlist))
print("Number of digits:", digits)
print("Number of uppercase letters:", upper)
print("Number of lowercase letters:", lower)
