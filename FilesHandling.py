# --------------------------------------
# ------ Files Handling Part 1 ---------
# --------------------------------------

import os

# Derectory For The Opened File
print(os.path.dirname(os.path.abspath(__file__)))

#This File
print(os.path.abspath(__file__))

# file = open(os.path.abspath(__file__))

print("=" * 30)

# ------------------------------------------
# ---- Files Handling Part 2 Read Files ----
# ------------------------------------------

myFile = open(os.path.abspath(__file__), "r")

# print(myFile) #File Data Object
# print(myFile.name)
# print(myFile.mode)
# print(myFile.encoding)

# print(myFile.read())
print(myFile.read(5))
print(myFile.readline())
# print(myFile.readlines())
# print(myFile.readline(5))

# print(type(myFile.readlines()))

for line in myFile:
    print(line)
    if line.startswith("#"):
        break

myFile.close()

print("=" * 30)

# ----------------------------------------------------
# - Files Handling Part 3 Write and Append In Files -
# ----------------------------------------------------

myFile = open("test.txt", "w")
myFile.write("hello\n")
myFile.write("Hello From Python File With Love\n")

print("=" * 30)

# ----------------------------------------------------
# ------- Files Handling Part 4 Important Info -------
# ----------------------------------------------------

# myFile = open("test.txt", "a")
# myFile.truncate(5)


myFile = open("test.txt", "r")
myFile.seek(6)
print(myFile.read())

os.remove("test.txt")