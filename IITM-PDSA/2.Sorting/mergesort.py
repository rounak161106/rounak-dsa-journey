def merge(left, right):
    # print(left, right)
    m = len(left)
    n = len(right)
    i = j = k = 0
    res = []
    while k != m+n:
        if i != m and j != n:
            if left[i] <= right[j]:
                res.append(left[i])
                i,k = i + 1, k + 1
            elif right[j] <= left[i]:
                res.append(right[j])
                j,k = j+1, k+1
        elif i == m:
            res.extend(right[j:])
            k = k + n-j
        else:
            res.extend(left[i:])
            k = k + m-i
    return res

# def merge(left, right):
#     m = len(left)
#     n = len(right)

#     i = j = 0
#     res = []

#     while i < m and j < n:
#         if left[i] <= right[j]:
#             res.append(left[i])
#             i += 1
#         else:
#             res.append(right[j])
#             j += 1

#     res.extend(left[i:])
#     res.extend(right[j:])

#     return res
        


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)

arr = eval(input("Enter a list to sort : "))
print("Before Sorting :",arr)
res = mergeSort(arr)
print("After Sorting :",res)