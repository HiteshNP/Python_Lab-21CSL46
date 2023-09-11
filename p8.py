"""Write a python program to find whether the given input is palindrome or not (for
both string and integer) using the concept of polymorphism and inheritance.
"""


class PaliStr:
    def chkPalindrome(self, myStr):
        return myStr == myStr[::-1]


class PaliInt(PaliStr):
    def chkPalindrome(self, val):
        temp = val
        rev = 0
        while temp != 0:
            dig = temp % 10
            rev = (rev * 10) + dig
            temp = temp // 10

        return val == rev


def main():
    st = input("Enter a string: ")
    stObj = PaliStr()

    if stObj.chkPalindrome(st):
        print("Given string is a Palindrome")
    else:
        print("Given string is not a Palindrome")

    val = int(input("Enter an integer: "))
    intObj = PaliInt()

    if intObj.chkPalindrome(val):
        print("Given integer is a Palindrome")
    else:
        print("Given integer is not a Palindrome")


if __name__ == "__main__":
    main()
