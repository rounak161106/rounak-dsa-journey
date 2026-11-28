def dfs_pre_post(adlist):
    pre, post = {},{}
    visited = {i:False for i in adlist}
    count = 1
    def dfs(v):
        nonlocal count
        pre[v] = count
        count += 1
        visited[v] = True
        for neighbour in adlist[v]:
            if not visited[neighbour]:
                dfs(neighbour)
        post[v] = count
        count += 1

    for i in adlist:
        if not visited[i]:
            dfs(i)
    return pre,post


digraph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': ['A', 'E'],  # D -> A creates a back edge (cycle)
    'E': [],
    'F': ['E']        # F can reach E, but F itself is not reachable from A
}
pre, post = dfs_pre_post(digraph)
print(pre)
print(post)