# Complexity of this algorithm with adjacency list is O(n+m) where n is the no. of vertices and m is the no. of edges.
from collections import deque

def bfs(ad_list, v):
    visited = {i:False for i in ad_list}
    parent = {i:-1 for i in ad_list}
    level = {i:-1 for i in ad_list}

    level[v] = 0
    visited[v] = True

    queue = deque()
    queue.append(v)

    while queue:
        curr_vertex = queue.popleft()
        for i in ad_list[curr_vertex]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                parent[i] = curr_vertex
                level[i] = level[curr_vertex] + 1
    print("Reachibility :",visited)
    print("Parent :",parent)
    print("Level :",level)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F', 'G'],
    'F': ['C', 'E'],
    'G': ['E']
}
bfs(graph, 'A')