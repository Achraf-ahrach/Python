a , b , c = 1, 2, 3

# print(a)
# print("11111\rabc")

a = '''first\
second "Test"\
third'''

# print(a[4:6])
# print(a[4:])
# print(a[:4])
# print(a[:])
# print(a[-3::2])

a = "ioI Love Python    io"

# print(a.strip(""))
# print(a.rstrip(""))
# print(a.lstrip(""))

# title

b = "I love 2d Graphics and 3g Technology and phthon"
# print(b.title())

# print(b.capitalize())

myMoney = ["achraf", "hello", 44, 1, True]
myFrinds = ["new", "one", 2, 3, False]

myMoney.append(myFrinds)
# print(myMoney[5][1])

# extend

a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

a.extend(b)
# print(a)
a.remove(6)
# print(a)
a.sort(reverse=True)
# print(a)
print("-" * 30)

a = {"A", "B", 4, "C", True, (1, 2, 3,4)}
b = {"A", "7"}
c = a | b

# b.update(['html', "css"])
# print(a.difference(b))

# difference and difference_update

# print(a.difference(b))
# print(a)
# a.difference_update(b)
# print(a)

# intersection_update()

g = {1, 2, 3, 4, "X", "Osama"}
h = {"Osama", "X", 2}
# print(g)
g.intersection_update(h)
# print(g)

# symmetric_difference()

i = {1, 2, 3, 4, 5, "X"}
j = {"Osama", "Zero", 1, 2, 4}
print(i)
print(i.symmetric_difference(j))
print(i)

