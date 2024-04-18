# ----------------------------------------
# --------- Built In Functions 1 ---------
# ----------------------------------------

x = [1, 2, 4, 7]

if all(x):
    print("All Ellements Is True")

else:
    print("There At Least One Element Is False")

x = [1, 8]

if any(x):
    print("There's At Least One Element Is True")

else:
    print("There No Any Element True Element")


print(bin(100))

a = 1;
b = 2;
print(id(a))
print(id(b))

print("-" * 30)

# sum() # round() # range() # print()

print("-" * 30)

# sume(iterable, start)

a = [1, 10, 19, 40]

print(f"sume = {sum(a)}")
print(f"sume = {sum(a, 40)}")

print("-" * 30)

# sume(number, numofdigits)

print(f"round = {round(150.499)}")
print(f"round = {round(150.499, 2)}")

print("-" * 30)
# range(start, end, step)

print(list(range(0)))
print(list(range(10)))
print(list(range(0, 21, 2)))

print("-" * 30)
# print()

print("Hello Achraf How Are You")
print("Hello", "Achraf", "How", "Are", "you")
print("Hello", "Achraf", "How", "Are", "you", sep="@")
print("First Line", end="\n")