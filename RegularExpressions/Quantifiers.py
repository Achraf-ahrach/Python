# ---------------------------------------------
# ------- Regular Expressions => Quantifiers --
# ---------------------------------------------

# https://pythex.org/


# --------------------------------------------------
# -- Regular Expressions => Re Module And FindAll --
# --------------------------------------------------

import re

my_search = re.search("[A-Z]", "achrafAhrach")

# print(my_search)
# print(dir(my_search))
# print(my_search.span())
# print(my_search.string)
# print(my_search.group())

# ========= example 2 ===========


# is_email = re.search(r"[A-z0-9\.]+@[A-z0-9]+\.(com|net)", "achrafahrch44@gmail.com")

# if is_email:

#     print("This is A Valid Email")

# else:
    
#     print("This is Not A Valid Email")


# ========= example 3 ===========


email_input = input("Please Write Your Email: ")

search = re.findall(r"[A-z0-9\.]+@[A-z0-9]+\.com|net", email_input)

empty_list = []

if search != empty_list :

    empty_list.append(search)

    print("Email Added")

else :
    print("Invalid Email")

for email in empty_list:
    print(email)

