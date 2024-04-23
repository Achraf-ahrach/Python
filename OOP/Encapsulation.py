# -----------------------------------------------------
# ---- Object Oriented Programing => Incapsulation ----
# ------------------------------------------------------

# class Member:

#     def __init__(self, name):
        
#         self.name = name # Public


# one = Member("Achraf")
# print(one.name)
# one.name = "Sayed"
# print(one.name)


# class Member:

#     def __init__(self, name):
        
#         self._name = name # protected


# one = Member("Achraf")
# print(one._name)
# one._name = "Sayed"
# print(one._name)

class Member:

    def __init__(self, name):
        
        self.__name = name # private
    
    def say_hello(self):

        return f"Hello {self.__name}"

one = Member("Achraf")
# print(one.__name)
print(one.say_hello())
print(one._Member__name)
