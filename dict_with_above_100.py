
my_dict1 = {}

n=int(input("Enter an nummber:"))
for i in range(n):
    key1=input("Enter Key:")
    value1=int(input("Enter value:"))
    my_dict1[key1]=value1
print(my_dict1)
for key1,value1 in my_dict1.items():
    if value1 > 100:
        print(key1,":" , value1)
