# ------------------------------------------
# ------ Date And Time => Formet Date ------
# ------------------------------------------

import datetime

myBirthday = datetime.datetime(2002, 12, 28)

print(myBirthday)
print(myBirthday.strftime("%a"))
print(myBirthday.strftime("%A"))
print(myBirthday.strftime("%b"))
print(myBirthday.strftime("%B"))

print(myBirthday.strftime("%d-%B-%Y"))