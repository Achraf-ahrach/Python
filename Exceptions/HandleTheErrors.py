# -----------------------------------------------------
# - Exceptions => Handling Try, Txcept, Else, Finally -
# -----------------------------------------------------

# try: 

#     number = int(input("Write Your Age: "))
#     print("Good, This Is Integer From Try")

# except:
    
#     print("This is Not Integer")

# else:

#     print("Good, This Is Integer From Else")

# finally:

#     print("Print From Finally Whataver Happens")


# -------- example 2 --------

try:
    # print(10 / 0)
    # print(e)
    print(int("Achraf"))

except ZeroDivisionError:

    print("Cant Divide")

except NameError:

    print("Identifier Not Found")

except ValueError:

    print("Value Error Achraf")

except:

    print("Error Happens")

