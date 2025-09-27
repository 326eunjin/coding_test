from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[False]*m for _ in range(n)]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    queue = deque()
    queue.append((0,0,1))  # x, y, distance
    visited[0][0] = True

    while queue:
        x, y, dist = queue.popleft()

        # 목표 도착
        if x == n-1 and y == m-1:
            return dist

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist+1))

    return -1  # 도달 불가
