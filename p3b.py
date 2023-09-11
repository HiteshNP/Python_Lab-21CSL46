"""Write a Python program to find the string similarity between two given strings"""

import difflib


def string_similarity(st1, st2):
    result = difflib.SequenceMatcher(None, st1, st2).ratio()
    return result


str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")
similarity = string_similarity(str1, str2)
print("String similarity:", similarity)
