from collections import deque

import sys

input = sys.stdin.readline


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


# def get_first_false(visited):
#     for i in range(1, len(visited)):
#         if visited[i] == False:
#             return i
#     return -1


n, l = map(int, input().split(" "))
graph = [[] for _ in range(n + 1)]
for i in range(l):
    tmp1, tmp2 = map(int, input().split(" "))
    graph[tmp1].append(tmp2)
    graph[tmp2].append(tmp1)

visited = [False] * (n + 1)
cnt = 0
# while True:
#     idx = get_first_false(visited)
#     if idx < 0:
#         break
#     bfs(graph, idx, visited)
#     cnt += 1

for i in range(1, n + 1):  # 1번부터 n번 노드까지 확인
    if not visited[i]:  # 아직 방문하지 않은 노드라면
        bfs(graph, i, visited)
        cnt += 1

print(cnt)
