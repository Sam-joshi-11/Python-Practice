l=[]
n=int(input("Enter an number:"))
for i in range(n):
    k=int(input("Enter the values:"))
    l.append(k)
print(f"The list is {l}")
r=int(input("Enter the number to be removed from the list:"))
t=int(input("ENter the number to be inserted in list:"))
q=l.index(r)
l.remove(r)
l.insert(q,t)
print(l)