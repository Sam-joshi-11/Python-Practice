# Ask the user to enter a number
num = int(input("Enter a number: "))

# Prime numbers are greater than 1
if num > 1:
    # Check for factors
    for i in range(2, num):
        # If num is divisible by any number between 2 and num-1, it's not prime
        if num % i == 0:
            print(num, "is not a prime number.")
            break
    else:
        # This else belongs to the for loop, not the if
        print(num, "is a prime number.")
else:
    # If the number is 1 or less, it's not prime
    print(num, "is not a prime number.")
