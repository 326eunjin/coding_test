from collections import deque

MAX = 100000
start, end = map(int, input().split())

dist = [-1] * (MAX + 1)
count = [0] * (MAX + 1)
count[start] = 1  # 시작점에서 출발하는 방법 1

queue = deque([start])
dist[start] = 0

while queue:
    x = queue.popleft()
    for nx in [x-1, x+1, x*2]:
        if 0 <= nx <= MAX:
            if dist[nx] == -1:  # 처음 방문
                dist[nx] = dist[x] + 1
                count[nx] = count[x]
                queue.append(nx)
            elif dist[nx] == dist[x] + 1:  # 같은 최소 시간으로 도달
                count[nx] += count[x]

print(dist[end])   # 최소 시간
print(count[end])  # 최소 시간으로 도달하는 경로 수
