# ----------------------------------------
# ----- Built In Functions => Reduce -----
# ----------------------------------------

from functools import reduce

def sumAll(num1, num2):
    return num1 + num2

numbers = [1, 8, 2, 9, 100]

result = reduce(sumAll, numbers)

print(result)

# Use Reduce With Lambda Function

print("\n== Use Reduce With Lambda Function ==")

result = reduce(lambda num1, num2: num1 + num2, numbers)

print(result)