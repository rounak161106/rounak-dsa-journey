# We know that DAG's are directly graphs without any cycles and it is true that every dag can be topologically sorted.
# Kahn's Algorithm
def topo_sort(adlist):
    indegree = {i:0 for i in adlist}
    for i in adlist:
        for j in adlist[i]:
            indegree[j] = indegree[j]+1
    l = []
    for i in adlist:
        vertex = [i for i in indegree if indegree[i]==0][0]
        indegree[vertex] = -1
        l.append(vertex)
        for neighbour in adlist[vertex]:
            indegree[neighbour] -= 1
    return(l)

from collections import deque
def topo_sort2(adlist): #complexity goes down to O(n+m)
    indegree = {i:0 for i in adlist}
    for i in adlist:
        for j in adlist[i]:
            indegree[j] = indegree[j]+1
    l = []
    queue = deque([i for i in indegree if indegree[i] == 0])
    while queue:
        vertex = queue.popleft()
        l.append(vertex)
        for neighbours in adlist[vertex]:
            indegree[neighbours] -= 1
            if indegree[neighbours] == 0:
                queue.append(neighbours)
    return l
dag = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['E'],
    'D': ['E'],
    'E': [],
    'F': ['E']
}
print(topo_sort(dag))
print(topo_sort2(dag))