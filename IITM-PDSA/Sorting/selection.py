#This is an inplace sorting and it is not stable

arr = eval(input("Enter the list of numbers: "))
print("Before Sorting :", arr)
for i in range(len(arr)):
    mini = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[mini]:
            mini = j
    arr[i], arr[mini] = arr[mini], arr[i]
print("After sorting :", arr)