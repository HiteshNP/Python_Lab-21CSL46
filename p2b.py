"""Develop a python program to convert binary to decimal, octal to hexadecimal using
functions."""


def binaryToDecimal(binary):
    decimal = int(binary, 2)
    return decimal


def octalToHexadecimal(octal):
    hexadecimal_value = hex(int(octal, 8)).replace("0x", "")
    return hexadecimal_value


binary_input = input("Enter a binary number: ")
decimal_result = binaryToDecimal(binary_input)
print("Decimal representation of", binary_input, "is", decimal_result)

octal_input = input("Enter an octal number: ")
hexadecimal_result = octalToHexadecimal(octal_input)
print("Hexadecimal representation of", octal_input, "is", hexadecimal_result)
