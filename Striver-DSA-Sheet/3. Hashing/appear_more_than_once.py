arr = [1, 2, 3, 2, 4, 1, 5]
freq = {}

for i in arr:
    freq[i] = freq.get(i,0)+1

for i in freq:
    if freq[i] > 1:
        print(i)

print(freq)