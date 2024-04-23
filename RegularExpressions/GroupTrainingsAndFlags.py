# ------------------------------------------------------
# -- Regular Expressions => Group Trainings And Flags --
# ------------------------------------------------------

import re

my_web = "https://www.Achraf-ahrach:8080/watch?v=MLb7pPOEJlg&list"

search = re.search(r"(https?)://(www)?\.?(\w+)\.(\w+):?(\d+)?\?(.+)", my_web) # ,re.I

# print(search.group())
# print(search.groups())


# print(f"Protocol: {search.group(1)}")
# print(f"Sub Domain: {search.group(2)}")
# print(f"Domain Name: {search.group(3)}")
# print(f"Top Level Domain: {search.group(4)}")
# print(f"port: {search.group(5)}")
# print(f"Query String: {search.group(6)}")
