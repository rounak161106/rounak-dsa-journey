# Write a function find_Min_Difference(L, P) that accepts a list L of integers and P (positive integer) where the size of L is greater than P. The task is to pick P different elements from the list L, where the difference between the maximum value and the minimum value in selected elements is minimum compared to other differences in possible subset of p elements. The function returns this minimum difference value.
# Note - The list can contain more than one subset of p elements that have the same minimum difference value.

# Example

# Let L = [3, 4, 1, 9, 56, 7, 9, 12, 13] and P = 5

# If we see the following two subsets of 5 elements from L

# [3, 4, 7, 9, 9] or [7, 9, 9, 12, 13]

# Here, the difference between the maximum value and the minimum value in both subset is 9 - 3 = 6 or 13 - 7 = 6 which is minimum. So the output will be 6.

l = [41900,69441,94407,37498,20299,10856,36221,2231,54526,79072,84309,76765,92282,13401,44698,17586,98455,47895,98889,65298,32271,23801,83153,12186,7453,79460,67209,54576,87785,47738,40750,31265,77990,93502,50364,75098,11712,80013,24193,35209,56300,85735,3590,24858,6780,50086,87549,7413,90444,12284,44970,39274,81201,43353,75808,14508,17389,10313,90055,43102,18659,20802,70315,48843,12273,78876,36638,17051,20478]
k = 5
l.sort()
m = float('inf')
for i in range(len(l) - k + 1):
    diff = l[i+k-1] - l[i]
    m = min(diff, m)

print(m)