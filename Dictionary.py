# () tuple
# [] list
# {} set
# {"" : ''} dictionary

# dictionary

user = {
    "name" : "achraf",
    "age" : 36,
    "country": "Morroco",
    "skills": ["C", "C++", "Python"]
}

# print(user)
# print(user.keys())
# print(user.values())
# print(user.get("country"))

# Two-Dimensional Dictionary

languages = {
    "One": {
        "name": "C",
        "progress": "90%"
    },
    "Two": {
        "name": "C++",
        "progress": "85%"
    },
    "Three": {
        "name": "Python",
        "progress": "70%"
    },
}

# print(languages)
# print(languages['One'])
# print(languages['Three']['name'])

# print(len(languages))
# print(len(languages("Two")))

# Items()

view = {
    "name" : "achraf",
    "skill": "XBox"
}

allItems = view.items()
# print(view)
view["age"] = 36

# print(allItems)

# fromkeys()

a = ('MyKeyOne', 'MyKeyTwo', 'MyKeyThree')
b = "X"

# print(dict.fromkeys(a, b))

# Membership Operarors

admins = ["Osama", "Achraf", "Mustapha", "Haitam", "Ali", "Mahmoud"]

name = input("Please Type Your Name: ").strip().capitalize()

if name in admins:
    print(f"Hello {name} Welcome Back")
    option = input("Delete Or Update Your Name ?").strip().capitalize()
    # Update Option
    if option == 'Update' or 'u':
        theNewName = input("Your New Name Please: ").strip().capitalize()
        admins[admins.index(name)] = theNewName
        print("Name Updated.")
    # Delete Option
    elif option == 'Delete' or 'd':
        admins.remove(name)
        print("Name Deleted")
    # Wrong Option
    else:
        print("Wrong Option Choosed")
else:
    print(f"You Are Not Admin {name}")
