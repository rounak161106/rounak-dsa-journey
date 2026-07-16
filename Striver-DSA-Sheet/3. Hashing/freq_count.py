arr = [-1, -2, -1, 0, -2, -2]
d = {}
for i in arr:
    d[i] = d.get(i,0) + 1
print(d)