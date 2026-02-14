arr = [-1, -2, -1, 0, -2, -2]
elements = set(arr)
x = int(input("Enter the value to find if it exists in the array"))
if x in elements:
    print("Exists")
else:
    print("Doesn't exists")