from collections import deque

MAX = 100000
start, end = map(int, input().split(" "))
dist = [-1] * (MAX + 1)


def bfs(start, dist):
    queue = deque([start])
    dist[start] = 0

    while queue:
        x = queue.popleft()

        dx = [x + 1, x - 1, x * 2]
        for d in dx:
            if 0 <= d <= MAX and dist[d] == -1:
                queue.append((d))
                dist[d] = dist[x] + 1
                if d == end:
                    break


bfs(start, dist)
print(dist[end])
