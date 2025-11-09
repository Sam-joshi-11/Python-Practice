"""
l=[]
n=int(input("Enter:"))
for i in range(n):
    k=int(input("Enter:"))
    l.append(k)
print(l)
print(max(l))
        
 """       
        
# Ask the user to enter the first number
largest = int(input("Enter number 1: "))

# Use a loop to get the remaining 4 numbers
for i in range(2, 6):
    num = int(input(f"Enter number {i}: "))
    if num > largest:
        largest = num  # Update 'largest' if a bigger number is found

# After the loop, print the largest number
print("The largest number is:", largest)
