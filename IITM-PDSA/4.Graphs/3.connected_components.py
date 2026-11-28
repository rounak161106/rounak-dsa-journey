# In bfs, the edges that are visited forms the edges of the tree and the edges that were there in the original graph but not in the tree forms a cycle. 
# In dfs, not all edges that are not a part of the tree contributes to cycle, we have to keep track of pre and post no. and construct the tree. 
# In case of directed graph, we have one more thing to note
# - There may be three types of edges which are not contributing to the tree :
# - Forward edge, Back edge and cross edge
# - Note that only back edges contribute to cycles
# - If there is an edge from u to v and [pre(u), post(u)] contains [pre(v), post(v)], means forward
# - If there is an edge from u to v and [pre(v), post(v)] contains [pre(u), post(u)], means backward
# - If there is no relation(intervals are disjoint), means cross

ad_list = {
    # Component 1: A, B, C, D, E
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B', 'E'],
    'E': ['D'],

    # Component 2: H, I
    'H': ['I'],
    'I': ['H'],

    # Component 3: K (isolated vertex)
    'K': []
}
def get_reachable(v):
    visited = {i:False for i in ad_list}
    def dfs(v):
        visited[v] = True
        for i in ad_list[v]:
            if not visited[i]:
                dfs(i)
    dfs(v)
    return visited

def component(ad_list):
    comp_id, seen = 1,0
    visited = {i:False for i in ad_list}
    component = {i:-1 for i in ad_list}

    while seen < len(ad_list):
        vertex = [v for v in ad_list if component[v] == -1]
        vertex = vertex[0]
        visited = get_reachable(vertex)
        for i in visited:
            if visited[i]:
                component[i] = comp_id
                seen += 1
        comp_id += 1
    return component


print(component(ad_list))

# More efficient code
def connected_components(ad_list):
    components, comp_id = {},0
    visited = {i:False for i in ad_list}
    def dfs(v, comp_id):
        visited[v] = True
        components[v] = comp_id
        for i in ad_list[v]:
            if not visited[i]:
                dfs(i, comp_id)
    for i in ad_list:
        if not visited[i]:
            comp_id += 1
            dfs(i, comp_id)
    return components

print(connected_components(ad_list=ad_list))