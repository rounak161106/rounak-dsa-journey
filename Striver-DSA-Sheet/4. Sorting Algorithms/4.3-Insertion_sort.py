# Program to sort an array in ascending order using insertion sort.
arr = [9, 8, 6, 3, 1]

for i in range(0, len(arr)):
    j = i
    while(j>0 and arr[j-1] > arr[j]):
        arr[j-1], arr[j] = arr[j], arr[j-1]
        j-=1
print(arr)