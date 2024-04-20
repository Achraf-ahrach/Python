# ----------------------------------------
# ----- Built In Functions => Filter -----
# ----------------------------------------

### Example 1 ###
 
# def chechNumber(num):
#     if num > 10:
#         return num

def chechNumber(num):
    return num > 10

myNumbers = [0, 0, 1, 55, 3, 21, 77]

myResult = filter(chechNumber, myNumbers)

for number in myResult:
    print(number)

print("=" * 30)

### Example 2 ###

def chechName(name):
    return name.startswith("O")

myNames = ["Achraf", "Osama", "Omer", "Ahmed", "Sayed", "Othman"]

myResult = filter(chechName, myNames)

for name in myResult:
    print(name)

print("=" * 5 , "Example Lambda Function", "=" * 5)

### Example 3 #####
# Lambda Function #

myResult = filter(lambda name : name.startswith("A"), myNames)

for name in myResult:
    print(name)