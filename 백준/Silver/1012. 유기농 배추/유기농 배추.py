from collections import deque

total = int(input())
result = []


def bfs(grid, start_x, start_y, visited):
    # 상하좌우 방향
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True

    while queue:
        x, y = queue.popleft()

        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]

            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] == 1 and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True


for _ in range(total):
    tmp_result = 0
    m, n, cnt = map(int, input().split(" "))
    grid = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    for _ in range(cnt):
        i, j = map(int, input().split(" "))
        grid[j][i] = 1
    for x in range(n):
        for y in range(m):
            if grid[x][y] == 1 and not visited[x][y]:
                bfs(grid, x, y, visited)
                tmp_result += 1
    result.append(tmp_result)

for r in result:
    print(r)
