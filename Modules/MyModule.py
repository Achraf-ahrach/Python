# ----------------------------------------
# ---- Modules => Create Your Module -----
# ----------------------------------------

# ------ add other path ------

# import sys
# sys.path.append(r"Games")
# print(sys.path)

# -----------------------------

 
import MyFunctions

MyFunctions.sayHowAreYou("Achraf")
MyFunctions.sayHello("Ahrach")

# -------- Alias --------------

print("\n----- Alias -----\n")

import MyFunctions as ee

MyFunctions.sayHello("Ahrach")
ee.sayHowAreYou("Achraf")

# ------ import one function of the module ------

print("\n--- import one function of the module ---\n")

from MyFunctions import sayHello
sayHello("Achraf")

# ------ change name function ------

from MyFunctions import sayHello as ss
ss("Achraf")