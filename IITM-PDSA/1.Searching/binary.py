n = eval(input("Enter the list of numbers: "))
ele = int(input("Enter the element to be searched: "))
found = False

low, high = 0, len(n)-1
while(low <= high):
    mid = (low + high) // 2
    if(ele > n[mid]):
        low = mid + 1
    elif(ele < n[mid]):
        high = mid - 1
    else:
        found = True
        print("Found at index :", mid)
        break

if not found:
    print("Not found")

#recursive way
def search(n, low, high, ele):
    if(low>high):
        return "Not Found"
    
    mid = (low + high)//2
    if(n[mid] == ele):
        return f"Found at index : {mid}"

    if(ele > n[mid]):
        return search(n, mid+1, high, ele)
    else:
        return search(n, low, mid-1, ele)

print(search(n, 0, len(n)-1, ele))
