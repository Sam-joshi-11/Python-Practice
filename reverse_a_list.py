l=[]
n=int(input("Enter the number:"))
for i in range(n):
    k=int(input("Enter the numbers:"))
    l.append(k)
print(f"List is {l}")
print(f"reversed list is {l[::-1]}")