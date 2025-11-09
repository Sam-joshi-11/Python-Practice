set1 = set(map(int, input("Enter the values for set1: ").split()))
set2 = set(map(int, input("Enter the values for set2: ").split()))

if set1.issubset(set2):   # checks whether all elements of set1 are in set2
    print("All elements of set1 are present in set2")
else:
    print("All elements of set1 are NOT present in set2")
