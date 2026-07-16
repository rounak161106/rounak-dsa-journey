arr = [4,12,13,3,11]
k = 11
pre = {0:0}
curr = 0
for i in arr:
    curr += i
    pre[curr] = arr.index(i)+1
    if curr - k in pre:
        print(arr[pre[curr-k]:arr.index(i)+1])


print(pre)