number = 350
if number > 100:
    print("A szám nagyobb, mint 100.")
else:
    print("A szám nem nagyobb, mint 100.")

if number % 2 == 0:
    print("szám páros")
else:
    print("nem páros")

num1 = 3
num2 = 9

if num1 % num2 == 0:
    print("oszthato")
elif num2 % num1 == 0:
    print("A másik szám osztható az elsővel.")
else:
    print("A számok nem oszthatók.")

str1 = "radar"

if str1[0] == str1[-1]:
    print("egyezik")
else:
    print("nem egyezeik")

num = 0
if num == 0:
    print("A szam nulla")
elif num > 0:
    print("pozitiv")
else:
    print("negativ")

a = 7
b = 4
c = 6

if a >= b and a >= c:
    print(a)

elif b >= a and b >= c:
    print(b)
else:
    print(c)

a = 3

if 3 <= a < 17:
    print("beleesik")
else:
    print("nem")

a = 3
b = 4
c = 5

if a+b>c or a+c>b or b+c>a:
    print("szerk")
else:
    print("nem")

'''try:
    osztalyazat = int(input())
except ValueError:
    print("no numbers")'''

print(type(float("3.5")))
print(type(str(7)))
print(type(str(-7.12)))

try:
    number=int(input())*3
    print(number)
except ValueError:
    print("Nem szám")
