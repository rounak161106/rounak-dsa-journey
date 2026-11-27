# You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9

# Output: [0,1]

# Explanation:

# The sum of nums[0] and nums[1] is 2 + 7 = 9, which equals the target. Therefore, the indices [0, 1] are returned.

# Example 2:

# Input: nums = [3,2,4], target = 6

# Output: [1,2]

# Explanation:

# The sum of nums[1] and nums[2] is 2 + 4 = 6, which equals the target. Therefore, the indices [1, 2] are returned..

arr = [2,7,11,15]
target = 9
arr = [(num, i) for i, num in enumerate(arr)]
arr.sort()
low = 0
high = len(arr)-1
while(low < high):
    sum = arr[low][0] + arr[high][0]
    if sum == target:
        print([arr[low][1], arr[high][1]])
        break
    if sum > target:
        high -= 1
    else:
        low += 1