is_number = False
number = 0
while not is_number:
    try:
        number = int(input("Kérek egy egész számot: "))
        is_number= True
    except ValueError:
        print("Ez nem egy egész szám.")

if number % 2 == 0:
    print("páros")
else:
    print("nem páros")

i = 1

while i<5:
    print(i)
    i+=1

for j in [1,2,3,4,5]:
    print(j)

for k in range(100):
    print(k,end=" ")

print()
for l in range(50,60):
    print(l, end=" ")

n=1
print()
while(n!=100):
    if n%2!=0:
        print(n, end=" ")
    n+=1


