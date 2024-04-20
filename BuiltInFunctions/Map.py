# ----------------------------------------
# ------ Built In Functions => Map -------
# ----------------------------------------

# Use MAP With Predefined Function

print("== Use MAP With Predefined Function ==")

def formatText(text):
    return f"- {text.strip().capitalize()} -"

myTexts = [" Osama ", "AhmEd", "  sAYed"]

myFormatedData = map(formatText, myTexts)

# print(myFormatedData)

for name in map(formatText, myTexts):
    print(name)

# Use MAP With Lambda Function

print("\n== Use MAP With Lambda Function ==")


for name in list(map(lambda text: f"- {text.strip().capitalize()} -", myTexts)):
    print(name)