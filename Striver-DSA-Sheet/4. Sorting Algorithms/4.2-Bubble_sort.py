# Program to sort an array in ascending order using bubble sort.
arr = [-5, 0, -2, 10, -1, -55, 123]

for i in range(len(arr)-1, 0, -1):
    for j in range(0, i):
        if arr[j] > arr[j+1]:
            arr[j+1], arr[j] = arr[j], arr[j+1]

print(arr)