my_dict = {}

n=int(input("Enter an nummber:"))
for i in range(n):
    key=input("Enter Key:")
    value=input("Enter value:")
    my_dict[key]=value
print(my_dict)
for key,value in my_dict.items():
    print(f"{key}:{value}")

my_dict.update({"course":"Data Science"})    
print(my_dict)

my_dict.update({"marks":"92"})
print(my_dict)