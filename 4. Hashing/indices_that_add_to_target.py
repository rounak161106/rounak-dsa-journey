arr = [2, 6, 11, 15,7]
target = 9
mp = {}

for i,x in enumerate(arr):
    if target-x in mp:
        print(mp[target-x],i)
    mp[x] = i