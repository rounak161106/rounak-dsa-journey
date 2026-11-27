# Complete the python function findLargest(L) below, which accepts a list L of unique numbers, that are sorted(ascending) and rotated n times, where n is unknown, and returns the largest number in list L. Rotating list [2, 4, 5, 7, 8] one time gives us list [8, 2, 4, 5, 7], and rotating the second time gives list [7, 8, 2, 4, 5] and so on. Try to give an 
# O(log n)
# O(log n)solution. Hint: One of the O(log n)
# O(log n) solutions can be implemented using binary search and using 'first or last' element to know, the direction of searching further.

# # input<L>: List L sorted and rotated.
# # out: Return the largest number in list L.
# def findLargest(L):
#     # Your code goes here
# Sample input:

# 7, 8, 2, 4, 5
# Sample output:

# 8
 

# Note:- Do not use list slicing in the binary search implementation because the list slicing operation is of order O(n).

arr = [8, 2, 4, 5, 7]
def findLargest(L):
    low = 0
    high = len(L) - 1

    # If the list is not rotated at all (or has 1 element), the last element is largest
    if L[low] <= L[high]:
        return L[high]

    while low <= high:
        mid = (low + high) // 2

        # Check if mid itself is the pivot (largest element)
        if mid < high and L[mid] > L[mid + 1]:
            return L[mid]

        # Check if mid - 1 is the largest element (mid is the smallest element)
        if mid > low and L[mid] < L[mid - 1]:
            return L[mid - 1]

        # Decide which half to search using the first element L[0]
        if L[mid] >= L[0]:
            # Left side from 0 to mid is strictly increasing, so the peak lies to the right
            low = mid + 1
        else:
            # L[mid] < L[0] means the drop-off happened before mid, so the peak lies to the left
            high = mid - 1
    
print(findLargest(arr))