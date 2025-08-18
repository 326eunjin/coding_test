from collections import deque


def dfs(graph, v, visited):
    visited[v] = True
    result.append(str(v))
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        result.append(str(v))
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n, m, v = map(int, input().split())
l = []
for _ in range(m):
    l.append(list(map(int, input().split(" "))))

graph = [[] for _ in range(n + 1)]
for i in l:
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])

for g in graph:
    g.sort()

visited = [False] * (n + 1)
result = []
dfs(graph, v, visited)
print(" ".join(result))
visited = [False] * (n + 1)
result = []
bfs(graph, v, visited)
print(" ".join(result))
