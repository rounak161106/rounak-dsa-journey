## Sorting is inplace and it is stable.

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if(arr[j] > arr[j+1]):
                swapped = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if not swapped:
            break

arr = eval(input("Enter a list to sort : "))
print("Before sorting :",arr)
bubbleSort(arr)
print("After sorting :",arr)

