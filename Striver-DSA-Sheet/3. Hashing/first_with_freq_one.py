arr = [4, 5, 1, 2, 0, 4]
freq = {}

for i in arr:
    freq[i] = freq.get(i,0) + 1

for i in freq:
    if freq[i] == 1:
        print(i)
        break

    