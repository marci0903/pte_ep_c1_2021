python = "python programozok"
print("A python szó 1. karaktere:", python[0])
print("A python szó utolsó karaktere:", python[5])
print("A python szó utolsó karaktere:", python[-1])
print("A python szó utolsó karaktere:", python[len(python)-1])
print("A python 5-ször egymás után:", python*5)

str1 = "hallgató"
str2 = "Hiába a hegynyi anyag, a hallgató gyorsan halad."
print(str1 in str2)
print(python in str2)
print(python not in str2)

print(str2[0:5])
print(python, str2, str1,sep=" alma ")

str4="HALLGATÓ"
print(str4 in str2)
print(str4 > str2)

