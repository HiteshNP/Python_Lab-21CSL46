"""Write a python program to accept a file name from the user and perform the following
operations
1. Display the first N line of the file
2. Find the frequency of occurrence of the word accepted from the user in the
file"""

import os.path
import sys


fname = input("Enter the filename: ")
n = int(input("Enter the number of lines to display: "))

if not os.path.isfile(fname):
    print("File", fname, "doesn't exist")
    sys.exit(0)

infile = open(fname, "r")
lineList = infile.readlines()
infile.close()

for i in range(0, n):
    print(i + 1, ":", lineList[i])
word = input("Enter a word: ")
cnt = 0
for line in lineList:
    cnt += line.count(word)
print(f"The word {word} appears {cnt} times in the file")
