def partition(arr, left, right):
    pivot = arr[left]
    i = left

    for j in range(left+1, right+1):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[left], arr[i] = arr[i], arr[left]
    return i

def quickSort(arr, left, right):
    if left < right:
        i = partition(arr, left, right)
        quickSort(arr, left, i-1)
        quickSort(arr, i+1, right)
    return arr

arr = eval(input("Enter a list to sort : "))
print("Before Sorting :",arr)
res = quickSort(arr, 0, len(arr) - 1)
print("After Sorting :",res)