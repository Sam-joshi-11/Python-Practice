l=[]
n=int(input("How many numbers you want to add in list:"))
for i in range(n):
    k=int(input("Enter an number:"))
    l.append(k)
print(f"items in the list are:{l}")
sum=0
for i in l:
    sum+=i
avg=sum/n
print(f"Sum of the nummber:{sum}\nAverage of nummber:{avg}")
