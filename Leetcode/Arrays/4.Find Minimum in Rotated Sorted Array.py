# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

 

# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
# Example 2:

# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times..

def findMin(self, nums: list[int]) -> int:
    low, high = 0, len(nums)-1
    if nums[low] <= nums[high]:
        return nums[low]
    while low <= high:
        mid = (low+high) // 2
        if mid<high and nums[mid] > nums[mid+1]:
            return nums[mid+1]
        elif mid > low and nums[mid] < nums[mid-1]:
            return nums[mid]
        elif nums[mid] < nums[0]:
            high = mid-1
        else:
            low = mid+1
print(findMin([3,4,5,1,2]))