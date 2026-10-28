#This is an implace sorting and it is 

arr = eval(input("Enter the list of numbers: "))
print("Before Sorting :", arr)
for i in range(len(arr)):
    mini = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[mini]:
            mini = j
    arr[i], arr[mini] = arr[mini], arr[i]
print("After sorting :", arr)