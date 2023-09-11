"""Write a program to convert roman numbers in to integer values using dictionaries."""


def roman_to_integer(roman_numeral):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    total = 0
    prev_value = 0

    for i in reversed(roman_numeral):
        value = roman_dict[i]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total


roman_input = input("Enter a Roman numeral: ")

result = roman_to_integer(roman_input.upper())
print("Roman Numeral:", roman_input, "\nInteger Value:", result)
