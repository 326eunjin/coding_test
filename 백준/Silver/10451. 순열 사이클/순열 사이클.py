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


num = int(input())
final = []
for _ in range(num):
    n = int(input())
    tmp = list(map(int, input().split(" ")))

    cnt = 0
    graph = [[] for _ in range(n + 1)]
    for i in range(len(tmp)):
        if i + 1 == tmp[i]:
            cnt += 1
        if tmp[i] not in graph[i + 1]:
            graph[i + 1].append(tmp[i])
        if i + 1 not in graph[tmp[i]]:
            graph[tmp[i]].append(i + 1)

    for g in graph:
        g.sort()

    total = []
    visited = [False] * (n + 1)
    for i in range(1, n + 1):
        result = []
        dfs(graph, i, visited)
        if sorted(result) not in total and len(result) != 1:
            total.append(result)

    final.append(cnt + len(total))

for f in final:
    print(f)