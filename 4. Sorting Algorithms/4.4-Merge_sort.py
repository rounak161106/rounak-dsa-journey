def merge(arr, low, mid, high):
    left = low
    right = mid+1
    temp = []
    while left <= mid and right <= high:
        if(arr[left] <= arr[right]):
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1

    while(left <= mid):
        temp.append(arr[left])
        left+=1

    while(right <= high):
        temp.append(arr[right])
        right+=1

    for i in range(low, high+1):
        arr[i] = temp[i-low]

def Merge_sort(arr, low, high):
    if low >= high:
        return
    
    mid = (low + high)//2
    Merge_sort(arr, low, mid)
    Merge_sort(arr, mid+1, high)
    merge(arr, low, mid, high)

arr = [13,245,23,64,2,1,62]
print(Merge_sort(arr, 0, 6))
print(arr)