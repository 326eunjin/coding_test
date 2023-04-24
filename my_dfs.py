def dfs(graph, visited, v):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    # ret = []
    # ret.append(v)
    # for i in len(graph[v]):
    #     if (visited[graph[v][i]] == False):
    #         ret.append(graph[v][i])
    #         visited[graph[v][i]] = True


graph = [[], [2, 3, 8], [1, 7], [1, 4, 5],
         [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
visited = [False]*9
dfs(graph, visited, 1)
