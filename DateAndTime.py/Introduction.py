# ------------------------------------------
# -- Date And Time => Introduction --
# ------------------------------------------

import datetime

# print(dir(datetime))
# print(dir(datetime.datetime))


# ----- Print The Current Date and Time ------

print(datetime.datetime.now())

print("#" * 40)

# ---- Print The Current Year ----

print(datetime.datetime.now().year)

# ---- Print The Current Month ----

print(datetime.datetime.now().month)

# ---- Print The Current Day ----

print(datetime.datetime.now().day)

print("#" * 40)

# ---- Print Start and End Of Date ---

print(datetime.datetime.min)
print(datetime.datetime.max)

print("#" * 40)

# print(dir(datetime.datetime.now()))

# ----- Print The Current Time ------

print(datetime.datetime.now().time())

print("#" * 40)

# ----- Print The Current Time Hour ------

print(datetime.datetime.now().time().hour)

# ----- Print The Current Time minute ------

print(datetime.datetime.now().time().minute)

# ----- Print The Current Time second ------

print(datetime.datetime.now().time().second)

print("#" * 40)
print(datetime.time.min)
print(datetime.time.max)

print("#" * 40)

# Print Specific Date
print(datetime.datetime(1900, 10, 25))
print(datetime.datetime(1900, 10, 25, 10, 45, 55, 150364))

print("#" * 40)

myBirthDay = datetime.datetime(2002, 12, 28)
dateNow = datetime.datetime.now()

print(f"My Birthday is {myBirthDay} and ", end="")
print(f"Date Now Is {dateNow}")

print(f" I Lived For {dateNow - myBirthDay}")
print(f" I Lived For {(dateNow - myBirthDay)} Days.")
print(f" I Lived For {(dateNow - myBirthDay).days / 365:.0f} years.")
