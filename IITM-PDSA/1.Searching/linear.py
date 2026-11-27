n = eval(input("Enter the list of numbers: "))
ele = int(input("Enter the element to be searched: "))
found = False

for i in range(len(n)):
    if n[i] == ele:
        found = True
        print("Found at index :",i)
        break

if(not found):
    print("Not found")