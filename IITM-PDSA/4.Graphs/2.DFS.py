# Complexity of this algorithm with adjacency list is O(n+m) where n is the no. of vertices and m is the no. of edges.
ad_list = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F', 'G'],
    'F': ['C', 'E'],
    'G': ['E']
}
visited = {i:False for i in ad_list}
parent = {i:-1 for i in ad_list}

def dfs2(v):
    visited[v] = True
    for j in ad_list[v]:
        if not visited[j]:
            parent[j] = v
            dfs2(j)

dfs2('A')
print(visited)
print(parent) 