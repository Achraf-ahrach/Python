# ----------------------------------------
# --------- Built In Functions 3 ---------
# ----------------------------------------
# enumerate()
# help()
# reversed()
# ----------------------------------------

# enumerate(iterable, start=0)

mySkills = ["Html", "Css", "Js", "PHP"]

mySkillsWithCounter = enumerate(mySkills, 20)

# print(type(mySkillsWithCounter))

for counter, skill in mySkillsWithCounter:
    print(f"{counter} - {skill}")

print("#" * 30)

##### help() ########

# print(help(print))

# print("#" * 30)

##### reversed() #####

myString = "Elzero"
print(reversed(myString))

for letter in reversed(myString):
    print(letter)