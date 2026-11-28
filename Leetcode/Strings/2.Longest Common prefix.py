# 14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.
strs =  ["flower","flow","flight"]
def solution(strs):
    for i in range(len(strs[0])):
        char = strs[0][i]
        for j in strs[1:]:
            if i==len(j) or j[i] != char:
                return strs[0][:i]
    return strs[0]
print(solution(strs))