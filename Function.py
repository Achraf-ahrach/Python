# -------------------------------------
# - Function Parameters And Arguments -
# -------------------------------------

a, b, c = "Achraf", "Ahmed", "Osama"

def say_hello(name):
    print(f"Hello {name}")

say_hello(a)
say_hello(b)
say_hello(c)

print("=" * 30)

def addition (n1, n2):
    if type(n1) != int or type(n2) != int:
        print("Only Integers Allowd")
    else:
        print(n1 + n2)

addition("100", 10)
addition(100, 10)

print("=" * 30)

def full_name(first, middle, last):
    print(f"Hello {first.strip().capitalize()} {middle.upper():.1s} {last.upper()}")

full_name("achraf", "achraf", "tn19n")

print("=" * 30)

# -----------------------------------------
# - Function Packing, Unpacking Arguments -
# -----------------------------------------

def say_hello(*peoples):
    for name in peoples:
        print(f"Hello {name}")

# say_hello("Achraf", "Mustapha", "amine", "Ali")
say_hello("Achraf", "Mustapha")

print("=" * 30)

# ------------------------------------
# ---  Function Default Parameters ---
# ------------------------------------

def say_hello(name, age="Unknown", country="Unknown"):
    print(f"Hello {name} Your Age is {age} and Your Country Is {country}")

say_hello("Achraf", 80, "agadir")
# say_hello("Achraf", 80)

print("=" * 30)

# -----------------------------------------
# -- Function Packing Unpacking Keyword ---
# -----------------------------------------

mySkills = {
    "Html": "80%",
    "C++": "70%",
    "C": "60%",
    "Python": "70%"
}

def show_skills(**skilles):
    print(type(skilles))
    for skill, value in skilles.items():
        print(f"{skill} = {value}")

show_skills(Html="80%", C="90", Python="80%", Js="20%")
print("-" * 20)
show_skills(**mySkills)