def reverse(arr):
    if len(arr) == 0:
        return []
    return [arr[-1]] + reverse(arr[:-1])

def reverse2(l,r,arr):
    if l>=r:
        return
    
    temp = arr[l]
    arr[l] = arr[r]
    arr[r] = temp

    reverse2(l+1,r-1,arr)

# print(reverse([1,2,3,4,5]))
arr = [1,2,3,4,5,5]
reverse2(0,5,arr)
print(arr)