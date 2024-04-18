
peoples = {
    "Ahmed": {
        "Html": "80%",
        "C++": "70%",
        "C": "60%",
        "Python": "70%"
    },
    "Achraf": {
        "Html": "10%",
        "C++": "30%",
        "C": "10%",
        "Python": "40%"
    },
    
    "Mustapha": {
        "Html": "60%",
        "C++": "70%",
        "C": "50%",
        "Python": "70%"
    },
    
    "Ali": {
        "Html": "80%",
        "C++": "70%",
        "C": "60%",
        "Python": "70%"
    },
}

for name in peoples:
    # print(f"name is: {name}")
    for languag in peoples[name]:
        pass
        # print(f"{languag.upper()} = {peoples[name][languag]}")

# ----------------------------------
# ---- Advanced Dictionary Loop ----
# ----------------------------------

mySkills = {
    "Html": "80%",
    "C++": "70%",
    "C": "60%",
    "Python": "70%"
}

# print(mySkills.items())
# for key, value in mySkills.items():
#     print(f"{key} = {value}")

    