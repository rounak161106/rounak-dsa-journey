# Program to sort an array in ascending order using selection sort.
arr = [-5, 0, -2, 10, -1]

for i in range(0, len(arr)-1):
    min = i 
    for j in range(i, len(arr)):
        if arr[j] < arr[min]:
            min = j

    temp = arr[i]
    arr[i] = arr[min]
    arr[min] = temp

print(arr)