# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Example 2:
# Input: height = [1,1]
# Output: 1
def maxArea(arr):
    left, right = 0, len(arr) - 1
    max_area = 0
    while(left < right):
        if(arr[left] <= arr[right]):
            area = (right-left) * arr[left]
            left += 1
        else:
            area = (right-left) * arr[right]
            right -= 1
        
        max_area = max(max_area, area)

    return max_area
print(maxArea([1,1]))