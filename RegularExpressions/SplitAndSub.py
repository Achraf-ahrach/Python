# ----------------------------------------------------
# -- Regular Expressions => Re Module Split And Sub --
# -----------------------------------------------------

import re

string_one = "I Love Python Programing Language"

search_one = re.split(r"\s", string_one)

print(search_one)

print("#" * 40)

string_two = "How-To_write_A_Very-Good-Article"

search_two = re.split(r"-|_", string_two)

print(search_two)


print("#" * 40)

for counter, word in enumerate(search_two, 1):
    if len(word) == 1:
        continue

    print(f"Word Number: {counter} => {word.lower()}")

print("#" * 40)

my_string = "I Love Python"

print(re.sub(r"\s", "-", my_string))

