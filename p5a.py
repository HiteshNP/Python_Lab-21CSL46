"""Write a function called isphonenumber () to recognize a pattern 415-555-4242 without
using regular expression and also write the code to recognize the same pattern using
regular expression.
"""

import re


def isphonenumber(phone_number):
    if len(phone_number) != 12:
        return False
    if not phone_number[:3].isdigit():
        return False
    if phone_number[3] != "-":
        return False
    if not phone_number[4:7].isdigit():
        return False
    if phone_number[7] != "-":
        return False
    if not phone_number[8:].isdigit():
        return False
    return True


def with_re(numstr):
    phno_pattern = re.compile(r'^\d{3}-\d{3}-\d{4}$')
    if phno_pattern.match(numstr):
        return True
    else:
        return False


ph_num = input("Enter the phone number:")
print("Without using regular expression")
if isphonenumber(ph_num):
    print("Valid phone number")
else:
    print("Invalid phone number")
print("Using regular expression")
if with_re(ph_num):
    print("Valid phone number")
else:
    print("Invalid phone number")
