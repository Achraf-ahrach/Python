# -------------------------------------------------------------------
# -- Object Oriented Programing => Instance Attributes and Methods --
# -------------------------------------------------------------------

class Member:

    def __init__(self, first_name, middle_name, last_name, gender):
        self.fname = first_name
        self.mname = middle_name
        self.lname = last_name
        self.gender = gender

    def full_name(self) :
        return(f"{self.fname} {self.mname} {self.lname}")

    def name_with_title(self) :

        if (self.gender == "Male"):
            return(f"Hello Mr {self.fname}")
        
        elif (self.gender == "Female"):
            return(f"Hello Miss {self.fname}")

        else:
            return(f"Hello {self.fname}")
        
    def get_all_info(self) :
        return(f"{self.name_with_title()}, Your Full Name Is: {self.full_name()}")

Member_one = Member("Achraf", "Ahrach", "Hoob", "Male")
Member_two = Member("Mustapha", "nawawi", "miim", "Male")
Member_three = Member("Mona", "Ali", "Boom", "Female")

# print(dir(Member_one))

# print(Member_one.fname, Member_one.mname, Member_one.fname)
# print(Member_two.fname, Member_two.mname, Member_two.fname)
# print(Member_three.fname, Member_three.mname, Member_three.lname)

print(Member_one.full_name())
print(Member_two.full_name())
print(Member_three.full_name())

print("#" * 40)

print(Member_one.name_with_title())
print(Member_two.name_with_title())
print(Member_three.name_with_title())

print("#" * 40)

print(Member_three.get_all_info())
