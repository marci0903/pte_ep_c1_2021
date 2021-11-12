my_list = [1,2.5,"alma", False]
print(len(my_list))
print(type(len(my_list)))

print("A 2 érték benne van-e a listában:", 2 in my_list)
print(type(2 in my_list))

print("A 2.5 érték benne van-e a listában:", 2.5 in my_list)

print("A 2.5 érték poziciója a listában.",my_list.index(2.5))


print(my_list[0])
print(my_list[-1])
print(my_list[0:2])
print(type(my_list))
my_list[0]=1.2
print(my_list[0])
my_list.append("körte")
print(my_list)

my_list.extend([1,2,3])
print(my_list)
my_list.insert(1,"tf")
print(my_list)