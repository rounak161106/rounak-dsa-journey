from collections import deque
def longest_path_to(adlist): #complexity goes down to O(n+m)
    indegree = {i:0 for i in adlist}
    longest_path = {i:0 for i in adlist}
    for i in adlist:
        for j in adlist[i]:
            indegree[j] = indegree[j]+1
    queue = deque([i for i in indegree if indegree[i] == 0])
    while queue:
        vertex = queue.popleft()
        for neighbours in adlist[vertex]:
            indegree[neighbours] -= 1
            longest_path[neighbours] = max(longest_path[neighbours],longest_path[vertex]+1)
            if indegree[neighbours] == 0:
                queue.append(neighbours)
    return longest_path
dag = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['E'],
    'D': ['E'],
    'E': [],
    'F': ['E']
}
print(longest_path_to(dag))