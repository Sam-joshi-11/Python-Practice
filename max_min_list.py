l=[]
n=int(input("Enter an number:"))
for i in range(n):
    k=int(input("Enter an value:"))
    l.append(k)
print(f"List is: {l}")
max=l[0]
min=l[0]
for i in l:
    if i>max:
        max=i
    if i<min:
        min=i
print(max)
print(min)