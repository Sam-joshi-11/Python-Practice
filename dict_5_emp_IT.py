
my_dict = {}

n=int(input("Enter an nummber:"))
for i in range(n):
    emp=input("Enter Employee name:")
    dep=input("Enter Department name:")
    my_dict[emp]=dep
print(my_dict)
for emp,dep in my_dict.items():
    if dep =="IT":
        print(emp,":" , dep)
