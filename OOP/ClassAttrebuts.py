# ----------------------------------------------------
# -- Object Oriented Programing => Class Attributes --
# ----------------------------------------------------

# -------------------------------------------------------------------
# -- Object Oriented Programing => Instance Attributes and Methods --
# -------------------------------------------------------------------

class Member:

    not_allowed_names = ["Hello", "Shit", "Baloot"]
    users_num = 0

    def __init__(self, first_name, middle_name, last_name, gender):
        self.fname = first_name
        self.mname = middle_name
        self.lname = last_name
        self.gender = gender
        Member.users_num += 1

    def full_name(self) :
        if self.fname in Member.not_allowed_names:
            raise ValueError("Name Not Allowed")

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
    
    def delete_user(self) :
        Member.users_num -= 1

        return(f"User {self.fname} Is Deleted.")

# print(dir(Member))

print(Member.users_num)

Member_one = Member("Achraf", "Ahrach", "Hoob", "Male")
Member_two = Member("Mustapha", "nawawi", "miim", "Male")
Member_three = Member("Mona", "Ali", "Boom", "Female")

print(Member.users_num)

print(Member_one.delete_user())

print(Member.users_num)

print("#" * 40)

# Member_one = Member("Hello", "Ahrach", "Hoob", "Male")

# print(Member.users_num)

# print(Member_one.full_name())