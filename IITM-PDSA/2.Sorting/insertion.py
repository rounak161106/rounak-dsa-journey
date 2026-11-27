#This is an inplace sorting and it is stable    
arr = eval(input("Enter a list to sort : "))
print("After sorting :",arr)
for i in range(1,len(arr)):
    j = i
    while(j>0 and arr[j] < arr[j-1]):
        arr[j], arr[j-1] = arr[j-1], arr[j]
        j -= 1

print("After sorting :",arr)

## Recusive way(stable but not inplace)
def insert(arr, ele):
    if not arr:
        return [ele]
    if ele >= arr[-1]:
        arr.append(ele)
        return arr
    else:
        return insert(arr[:-1], ele) + [arr[-1]]

def insertionSort(arr):
    n = len(arr)
    if n < 1:
        return []
    return insert(insertionSort(arr[:-1]), arr[-1])

print(insertionSort(arr))