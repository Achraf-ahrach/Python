# ----------------------------------------
# --------- Built In Functions 2 ---------
# ----------------------------------------

# abs()
# pow()
# min()
# max()
# slice()
# ------------------

# abs()

print(abs(100))
print(abs(-100))
print(abs(10.19))
print(abs(-10.19))

print("#" * 30)

#pow(base, exponent, mod) => Power
print(pow(2, 5))
print(pow(2, 5, 10)) # (2^5) % 10

print("#" * 30)

# min(item, item, item..., or iterator)
print(min(1, 10, -50, 20, 30))
print(min("A", "X", "Z", "Osama"))

myNumbers = (1, 20, -50, -100, 100)
print(min(myNumbers))

print("#" * 30)


# max(item, item, item..., or iterator)

print(max(1, 10, -50, 20, 30))
print(max("A", "X", "Z", "Osama"))

myNumbers = (1, 20, -50, -100, 100)
print(max(myNumbers))
