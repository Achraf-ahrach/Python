# ----------------------------------------------------
# ---- Object Oriented Programing => Polymorphism ----
# -----------------------------------------------------

n1 = 10
n2 = 20

print(n1 + n2)

s1 = "Hello"
s2 = "Python"

print(s1 + " " + s2)

print(len([1, 2, 3, 4, 5, 6]))
print(len(["Achraf Ahrach"]))

print(len({"Key_One": 1, "Key_Two": 2}))

print("#" * 30)

class A:

    def do_something(self):

        print("From Class A")

        raise NotImplementedError("Derived Class Must Implement This Method")


class B(A):
    
    def do_something(self):

        print("From Class B")

class C(A):
    
    def do_something(self):

        print("From Class C")


my_instance = B()
my_instance.do_something()