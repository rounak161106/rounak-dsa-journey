# Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
 

# Example 1:

# Input: timePoints = ["23:59","00:00"]
# Output: 1
# Example 2:

# Input: timePoints = ["00:00","23:59","00:00"]
# Output: 0

def convert(time):
    hr = int(time.split(":")[0])
    min = int(time.split(":")[1])
    return hr*60 + min

def findMinDifference(arr):
    if len(arr) > 1440:
        return 0 # because in 24 hours, we have 1440 unique minutes, if lenght exceed 1440, means one of the minute is repeated and so diff would be 0
    arr = list(map(convert, arr))
    arr.sort()
    n = len(arr)
    mini = 1440 - arr[n-1] + arr[0] # first we subracted arr[n-1] from 1440 in order to get the minutes left until midnight and then added arr[0] for how much time has passed after midnight. in this way we got the diff between first and last time.
    for i in range(n-1):
        mini = min(arr[i+1] - arr[i], mini)
    return mini
print(findMinDifference(["00:00","23:59","00:00"]))