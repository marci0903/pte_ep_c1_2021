import random

print(random.randint(2, 4))
print(random.random())

num = random.randint(-100, 100)
if num == 0:
    print("A szam nulla")
elif num > 0:
    print("pozitiv")
else:
    print("negativ")




