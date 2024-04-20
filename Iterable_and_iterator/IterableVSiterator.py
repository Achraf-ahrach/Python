# ------------------------------------------
# ---------- Iterable vs Iterator ----------
# ------------------------------------------

# Iterable
# [1] Object Contains Data That Can Be Iterated Upon
# [2] Examles (String, List, Set, Tuple, Dictionary)
# ----------------------------------------------
# Iterator
# [1] Object Used To Iterate Over Iterable Using next() Method Return 1 Element At A Time
# [2] You Can Generate Iterator From Iterable When Using iter() Method
# [3] For Loop Already Calls iter() Method on The Iterable Behind The Scene
# ----------------------------------------------

myString = "Achraf"

myList = [1, 2, 3, 4, 5]

for letter in myString:
    
    print(letter, end=" ")

for number in myList:
    print(number, end=" ")

print()
print("#" * 30)

myIterator = iter(myString)

print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))

print("#" * 30)

for letter in "Elzero": # for letter in iter("Elzero"):
    print(letter, end=" ")

print()